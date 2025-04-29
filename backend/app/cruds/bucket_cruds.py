''' Bucket CRUDs

Contains all the base functionailities for reading and writing bucket data into the database
5 base functionality:
- Create
- Read All instance
- Read an instance given an ID
- Update an instance given an ID
- Delete an instance given an ID

'''

from fastapi import HTTPException
from sqlmodel import Session, select

import app.models.bucket_models as models


def create_bucket(db: Session, new_bucket: models.BucketCreate):
    
    db_bucket = models.Bucket.model_validate(new_bucket)

    db.add(db_bucket)
    db.commit()
    db.refresh(db_bucket)

    return db_bucket

def get_all_buckets(db: Session, offset: int = 0, limit: int = 100):
    bucket = db.exec(select(models.Bucket).offset(offset).limit(limit)).all()
    return bucket

def get_bucket_by_id(db: Session, bucket_id: int):

    bucket = db.get(models.Bucket, bucket_id)

    if not bucket:
        raise HTTPException(status_code=404, detail="Bucket not found")
    
    return bucket

def update_bucket_by_id(db: Session, bucket_id: int, new_bucket: models.BucketUpdate):
    bucket_db = db.get(models.Bucket, bucket_id)
    
    if not bucket_db:
        raise HTTPException(status_code=404, detail="Bucket not found")
    
    bucket_data = new_bucket.model_dump(exclude_unset=True)
    bucket_db.sqlmodel_update(bucket_data)

    db.add(bucket_db)
    db.commit()
    db.refresh(bucket_db)

    return bucket_db

def delete_bucket_by_id(db: Session, bucket_id: int):
    bucket = db.get(models.Bucket, bucket_id)

    if not bucket:
        raise HTTPException(status_code=404, detail="Bucket not found")
    
    db.delete(bucket)
    db.commit()

    return {"Success": True}
