from typing import List, Dict

from app.utils.helpers import get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.api.schemas.bucket_schemas as schemas
import app.api.cruds.bucket_cruds as cruds

router = APIRouter()

# ======== BUCKET ENDPOINT ========


@router.post("/bucket", response_model=schemas.BucketReadNR, tags=['Bucket'])
def create_bucket(bucket: schemas.BucketCreate, db: Session = Depends(get_db)):
    return cruds.create_bucket(db=db, bucket=bucket)


@router.get("/buckets", response_model=List[schemas.BucketReadNR], tags=['Bucket'])
def get_all_buckets(limit: int = 50, db: Session = Depends(get_db)):
    return cruds.get_all_buckets(db=db, limit=limit)


@router.get('/bucket/{bucket_id}', response_model=schemas.BucketReadWR, tags=['Bucket'])
def get_bucket_by_id(bucket_id: int, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db=db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return db_bucket


@router.patch('/bucket/{bucket_id}', response_model=schemas.BucketReadWR, tags=['Bucket'])
def update_bucket_by_id(bucket_id: int, new_bucket: schemas.BucketUpdate, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db=db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return cruds.update_bucket_by_id(db=db, id=bucket_id, new_bucket=new_bucket)


@router.delete('/bucket/{bucket_id}', tags=['Bucket'])
def delete_bucket_by_id(bucket_id: int, db: Session = Depends(get_db)):
    db_bucket = cruds.get_bucket_by_id(db, id=bucket_id)
    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    return cruds.delete_bucket_by_id(db, id=bucket_id)
