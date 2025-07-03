from datetime import datetime

import app.models.bucket_models as model
import app.schemas.bucket_schemas as schemas
from sqlalchemy.orm import Session


def create_bucket(db: Session, bucket: schemas.BucketCreate, curr_date: datetime = datetime.now()):
    ''' Creating an new pet bucket '''

    db_bucket = model.Bucket(
        name=bucket.name,
        description=bucket.description,
        amount=bucket.amount,
        bucket_type=bucket.bucket_type,
        properties=bucket.properties.model_dump() if bucket.properties else None,
        created_at=curr_date,
        updated_at=curr_date
    )

    db.add(db_bucket)
    db.commit()
    db.refresh(db_bucket)
    return db_bucket


def get_all_buckets(db: Session, skip: int = 0, limit: int = 100, all: bool = False):
    ''' Get every instance of pet bucket, using offset pagination '''

    query = db.query(model.Bucket)

    total = query.count()
    data = query.all() if all else query.offset(skip).limit(limit).all()

    return schemas.BucketAllRead.model_validate({
        "total": total,
        "data": data
    }, from_attributes=True)


def get_bucket_by_id(db: Session, id: int):
    ''' Get specific instance of bucket based on provided bucket ID '''
    db_bucket = db.query(model.Bucket).filter(model.Bucket.id == id).first()
    return db_bucket


def get_bucket_by_name(db: Session, name: str):
    ''' Get specific instance of bucket based on provided bucket name (case insensitive) '''
    db_bucket = db.query(model.Bucket).filter(
        model.Bucket.name.ilike(name)).first()
    return db_bucket


def update_bucket_by_id(db: Session, id: int, new_bucket: schemas.BucketUpdate):
    ''' Update specific fields of specified instance of bucket on provided bucket ID '''
    db_bucket = db.query(model.Bucket).filter(model.Bucket.id == id).first()

    # Converts new_bucket from model object to dictionary
    update_bucket = new_bucket.model_dump(exclude_unset=True)

    # Loops through dictionary and update db_bucket
    for key, value in update_bucket.items():
        setattr(db_bucket, key, value)

    setattr(db_bucket, "updated_at", datetime.now())

    db.add(db_bucket)
    db.commit()
    db.refresh(db_bucket)
    return db_bucket


def delete_bucket_by_id(db: Session, id: int):
    ''' Delete specified instance of bucket on provided bucket ID '''
    db_bucket = db.query(model.Bucket).filter(model.Bucket.id == id).first()

    db.delete(db_bucket)
    db.commit()
    return {"Success": True}
