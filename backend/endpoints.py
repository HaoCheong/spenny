from typing import List

from helpers import get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import cruds
import schemas
import helpers

router = APIRouter()

# ======== MEALS ENDPOINT ========


@router.post("/bucket", response_model=schemas.BucketReadNR, tags=['bucket'])
def create_bucket(bucket: schemas.BucketCreate, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db, bucket=bucket.id)

    if db_bucket:
        raise HTTPException(status_code=400, detail="Bucket already exist")

    return cruds.create_bucket(db=db, bucket=bucket)


@router.get("/buckets", response_model=List[schemas.BucketReadNR], tags=['bucket'])
def get_all_buckets(limit: int = 10, db: Session = Depends(get_db)):
    return cruds.get_all_buckets(db=db, limit=limit)


@router.get('/buckets/{bucket_id}', response_model=schemas.BucketReadWR, tags=['bucket'])
def get_bucket_by_id(bucket_id: int, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db=db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return db_bucket


@router.patch('/bucket/{bucket_id}', response_model=schemas.BucketReadWR, tags=['bucket'])
def update_bucket_by_id(bucket_id: int, new_bucket: schemas.BucketUpdate, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db=db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return cruds.update_bucket_by_id(db=db, id=bucket_id, new_bucket=new_bucket)


@router.delete('/bucket/{bucket_id}', tags=['bucket'])
def delete_bucket_by_id(bucket_id: int, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return cruds.delete_bucket_by_id(db, id=bucket_id)
