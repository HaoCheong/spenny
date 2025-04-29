from typing import List

from app.helpers import get_db
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import app.schemas.bucket_schemas as schemas
import app.cruds.bucket_cruds as cruds

router = APIRouter()


@router.post("/api/v1/bucket", response_model=schemas.BucketReadNR, tags=["Buckets"])
def create_bucket(bucket: schemas.BucketCreate, db: Session = Depends(get_db)):
    return cruds.create_bucket(db=db, bucket=bucket)


@router.get("/api/v1/buckets", response_model=List[schemas.BucketReadNR], tags=["Buckets"])
def get_all_buckets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_buckets = cruds.get_all_buckets(db, skip, limit)
    return db_buckets


@router.get("/api/v1/bucket/{bucket_id}", response_model=schemas.BucketReadWR, tags=["Buckets"])
def get_bucket_by_id(bucket_id: int, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return db_bucket


@router.patch("/api/v1/bucket/{bucket_id}", response_model=schemas.BucketReadNR, tags=["Buckets"])
def update_bucket_by_id(bucket_id: int, new_bucket: schemas.BucketUpdate, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return cruds.update_bucket_by_id(db, id=bucket_id, new_bucket=new_bucket)


@router.delete("/api/v1/bucket/{bucket_id}", tags=["Buckets"])
def delete_bucket_by_id(bucket_id: int, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return cruds.delete_bucket_by_id(db, id=bucket_id)
