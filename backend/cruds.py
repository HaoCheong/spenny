from sqlalchemy.orm import Session
import models
import schemas


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


def get_all_buckets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bucket).offset(skip).limit(limit).all()


def get_bucket_by_id(db: Session, id: int):
    return db.query(models.Bucket).filter(models.Bucket.id == id).first()


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
    db_flowEvent = models.FlowEvent(
        name=flowEvent.name,
        description=flowEvent.description,
        change_amount=flowEvent.change_amount,
        frequency=flowEvent.frequency,
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
