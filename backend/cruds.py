from sqlalchemy.orm import Session
from sqlalchemy import desc
import models
import schemas
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from helpers import add_time


# {from_events: [], to_events:[]}
def get_bucket_flowEvents(db: Session, bucket_id: int):
    fromEvents = db.query(models.FlowEvent).filter(
        models.FlowEvent.from_bucket_id == bucket_id).all()
    toEvents = db.query(models.FlowEvent).filter(
        models.FlowEvent.to_bucket_id == bucket_id).all()

    return {"from_events": fromEvents, "to_events": toEvents}

# ========== CRUDS ==========


def create_bucket(db: Session, bucket: schemas.BucketCreate):
    db_bucket = models.Bucket(
        name=bucket.name,
        description=bucket.description,
        current_amount=bucket.current_amount
    )

    db.add(db_bucket)
    db.commit()
    db.refresh(db_bucket)
    return db_bucket


# Should return all the buckets and their
def get_all_buckets(db: Session, skip: int = 0, limit: int = 100):
    # all_buckets = []
    buckets = db.query(models.Bucket).offset(skip).limit(limit).all()
    # for bucket in buckets:
    #     je_bucket = jsonable_encoder(bucket)
    #     flowEvents = get_bucket_flowEvents(db=db, bucket_id=bucket.id)
    #     je_bucket['from_events'] = flowEvents["from_events"]
    #     je_bucket['to_events'] = flowEvents["to_events"]
    #     all_buckets.append(je_bucket)

    return buckets


def get_bucket_by_id(db: Session, id: int):
    bucket = jsonable_encoder(
        db.query(models.Bucket).filter(models.Bucket.id == id).first())
    flowEvents = get_bucket_flowEvents(db=db, bucket_id=id)
    bucket['from_events'] = flowEvents["from_events"]
    bucket['to_events'] = flowEvents["to_events"]
    return bucket


def update_bucket_by_id(db: Session, id: int, new_bucket: schemas.BucketUpdate):
    db_bucket = db.query(models.Bucket).filter(models.Bucket.id == id).first()

    # Converts new_owner from model.object to dictionary
    update_bucket = new_bucket.dict(exclude_unset=True)

    # Loops through dictionary and update db_owner
    for key, value in update_bucket.items():
        setattr(db_bucket, key, value)

    db.add(db_bucket)
    db.commit()
    db.refresh(db_bucket)
    return db_bucket


def delete_bucket_by_id(db: Session, id: int):
    db_bucket = db.query(models.Bucket).filter(models.Bucket.id == id).first()

    db.delete(db_bucket)
    db.commit()
    return {"Success": True}

# ======== FLOW EVENTS ========


def create_flowEvent(db: Session, flowEvent: schemas.FlowEventCreate):

    # Find the next date of trigger
    # Get the frequency + the current date time
    curr_time = datetime.now()
    print("CURR", curr_time)
    next_date = add_time(curr_time, flowEvent.frequency)

    db_flowEvent = models.FlowEvent(
        name=flowEvent.name,
        description=flowEvent.description,
        change_amount=flowEvent.change_amount,
        frequency=flowEvent.frequency,
        next_trigger=next_date,
        type=flowEvent.type,
        from_bucket_id=flowEvent.from_bucket_id,
        to_bucket_id=flowEvent.to_bucket_id
    )

    db.add(db_flowEvent)
    db.commit()
    db.refresh(db_flowEvent)
    return db_flowEvent


def get_all_flowEvents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FlowEvent).offset(skip).limit(limit).all()


def get_flowEvent_by_id(db: Session, id: int):
    return db.query(models.FlowEvent).filter(models.FlowEvent.id == id).first()


def update_flowEvent_by_id(db: Session, id: int, new_flowEvent: schemas.FlowEventUpdate):
    db_flowEvent = db.query(models.FlowEvent).filter(
        models.FlowEvent.id == id).first()

    # Converts new_owner from model.object to dictionary
    update_flowEvent = new_flowEvent.dict(exclude_unset=True)

    # Loops through dictionary and update db_owner
    for key, value in update_flowEvent.items():
        setattr(db_flowEvent, key, value)

    db.add(db_flowEvent)
    db.commit()
    db.refresh(db_flowEvent)
    return db_flowEvent


def delete_flowEvent_by_id(db: Session, id: int):
    db_flowEvent = db.query(models.FlowEvent).filter(
        models.FlowEvent.id == id).first()

    db.delete(db_flowEvent)
    db.commit()
    return {"Success": True}


# ======== LOG ========

def create_log(db: Session, log: schemas.LogCreate):
    db_log = models.Log(
        name=log.name,
        description=log.description,
        amount=log.amount,
        type=log.type,
        date_created=log.date_created,
        bucket_id=log.bucket_id
    )

    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_all_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Log).offset(skip).limit(limit).all()

# Get all the logs for a bucket after a specified date


def get_all_logs_by_bucket_id(db: Session, bucket_id: int, date: str):
    cap_date = datetime.strptime(date, "%d-%m-%Y")
    return db.query(models.Log).filter(models.Log.bucket_id == bucket_id).filter(models.Log.date_created > cap_date).order_by(desc(models.Log.date_created)).all()


def get_log_by_id(db: Session, id: int):
    return db.query(models.Log).filter(models.Log.id == id).first()


def update_log_by_id(db: Session, id: int, new_log: schemas.LogUpdate):
    db_log = db.query(models.Log).filter(
        models.Log.id == id).first()

    # Converts new_owner from model.object to dictionary
    update_log = new_log.dict(exclude_unset=True)

    # Loops through dictionary and update db_owner
    for key, value in update_log.items():
        setattr(db_log, key, value)

    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def delete_log_by_id(db: Session, id: int):
    db_log = db.query(models.Log).filter(
        models.Log.id == id).first()

    db.delete(db_log)
    db.commit()
    return {"Success": True}
