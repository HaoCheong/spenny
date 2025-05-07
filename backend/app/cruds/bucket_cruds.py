from sqlalchemy.orm import Session

import app.models.bucket_models as model
import app.schemas.bucket_schemas as schemas


def create_bucket(db: Session, bucket: schemas.BucketCreate):
    ''' Creating an new pet bucket '''

    db_bucket = model.Bucket(
        name=bucket.name,
        description=bucket.description,
        amount=bucket.amount,
        is_invisible=bucket.is_invisible,
        created_at=bucket.created_at,
        updated_at=bucket.updated_at
    )

    db.add(db_bucket)
    db.commit()
    db.refresh(db_bucket)
    return db_bucket


def get_all_buckets(db: Session, skip: int = 0, limit: int = 100):
    ''' Get every instance of pet bucket, using offset pagination '''

    query = db.query(model.Bucket)

    total = query.count()
    data = query.offset(skip).limit(limit).all()

    return {
        "total": total,
        "data": data
    }


def get_bucket_by_id(db: Session, id: str):
    ''' Get specific instance of bucket based on provided bucket ID '''
    return db.query(model.Bucket).filter(model.Bucket.id == id).first()


def update_bucket_by_id(db: Session, id: int, new_bucket: schemas.BucketUpdate):
    ''' Update specific fields of specified instance of bucket on provided bucket ID '''
    db_bucket = db.query(model.Bucket).filter(model.Bucket.id == id).first()

    # Converts new_bucket from model object to dictionary
    update_bucket = new_bucket.dict(exclude_unset=True)

    # Loops through dictionary and update db_bucket
    for key, value in update_bucket.items():
        setattr(db_bucket, key, value)

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
