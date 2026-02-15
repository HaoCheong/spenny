from typing import List

import app.cruds.bucket_cruds as cruds
# import app.operations.event_operations as event_op
import app.schemas.bucket_schemas as schemas
from app.helpers import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

'''
{
  "name": "Bucket A",
  "description": "Bucket A for Andrew",
  "amount": 5000,
  "bucket_type": "STORE",
  "properties": {}
}

{
  "name": "Bucket B",
  "description": "Bucket b for Bandrew",
  "amount": 3000,
  "bucket_type": "STORE",
  "properties": {}
}
'''

router = APIRouter()

@router.post("/api/v1/bucket", response_model=schemas.BucketReadWR, tags=["Buckets"])
def create_bucket(bucket: schemas.BucketCreate, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)

    # Check if the bucket with the shared name already exist
    db_bucket = cruds.get_bucket_by_name(db=db, name=bucket.name)
    if db_bucket:
        raise HTTPException(
            status_code=400, detail=f"Bucket called {bucket.name} already exists.")

    return cruds.create_bucket(db=db, bucket=bucket)


@router.get("/api/v1/buckets", response_model=schemas.BucketAllRead, tags=["Buckets"])
def get_all_buckets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)
    db_bucket_data = cruds.get_all_buckets(db, skip, limit)
    return db_bucket_data


@router.get("/api/v1/bucket/{bucket_id}", response_model=schemas.BucketReadWR, tags=["Buckets"])
def get_bucket_by_id(bucket_id: int, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)
    db_bucket = cruds.get_bucket_by_id(db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return db_bucket


@router.patch("/api/v1/bucket/{bucket_id}", response_model=schemas.BucketReadNR, tags=["Buckets"])
def update_bucket_by_id(bucket_id: int, new_bucket: schemas.BucketUpdate, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)
    db_bucket = cruds.get_bucket_by_id(db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return cruds.update_bucket_by_id(db, id=bucket_id, new_bucket=new_bucket)


@router.delete("/api/v1/bucket/{bucket_id}", tags=["Buckets"])
def delete_bucket_by_id(bucket_id: int, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)
    db_bucket = cruds.get_bucket_by_id(db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return cruds.delete_bucket_by_id(db, id=bucket_id)
