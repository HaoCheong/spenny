import app.api.models.bucket_model as bucket_model
import app.api.models.flow_event_model as flow_event_model
import app.api.schemas.bucket_schemas as schemas
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def get_bucket_flowEvents(db: Session, bucket_id: int):
    fromEvents = db.query(flow_event_model.FlowEvent).filter(
        flow_event_model.FlowEvent.from_bucket_id == bucket_id).all()
    toEvents = db.query(flow_event_model.FlowEvent).filter(
        flow_event_model.FlowEvent.to_bucket_id == bucket_id).all()

    return {"from_events": fromEvents, "to_events": toEvents}

# ========== CRUDS ==========
def create_bucket(db: Session, bucket: schemas.BucketCreate):
    db_bucket = bucket_model.Bucket(
        name=bucket.name,
        description=bucket.description,
        current_amount=bucket.current_amount,
        properties=jsonable_encoder(bucket.properties)
    )

    db.add(db_bucket)
    db.commit()
    db.refresh(db_bucket)
    return db_bucket


# Should return all the buckets and their
def get_all_buckets(db: Session, skip: int = 0, limit: int = 100):
    buckets = db.query(bucket_model.Bucket).offset(skip).limit(limit).all()
    return buckets


def get_bucket_by_id(db: Session, id: int):
    bucket = db.query(bucket_model.Bucket).filter(bucket_model.Bucket.id == id).first()
    return bucket


def update_bucket_by_id(db: Session, id: int, new_bucket: schemas.BucketUpdate):
    db_bucket = db.query(bucket_model.Bucket).filter(bucket_model.Bucket.id == id).first()

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
    db_bucket = db.query(bucket_model.Bucket).filter(bucket_model.Bucket.id == id).first()

    db.delete(db_bucket)
    db.commit()
    return {"Success": True}