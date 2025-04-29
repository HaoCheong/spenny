''' Bucket Endpoints

Contains all the function that subsequently call the bucket CRUD functions (see CRUD files)
Split was done because it allowed for simplified data validation and db calling.
- Endpoints: Takes in and validates input correctness
- CRUD: Focused on the logic of formatting and manipulating data, under the assumption that the provided data was correct

'''

from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

import app.cruds.bucket_cruds as cruds
import app.models.bucket_models as models
from app.database.database import SessionDep

router = APIRouter()

@router.post("/bucket/", response_model=models.BucketReadNR, tags=['Buckets'])
def create_bucket(bucket: models.BucketCreate, db: SessionDep):
    db_bucket = cruds.create_bucket(db=db, new_bucket=bucket)
    return db_bucket

@router.get("/buckets/", response_model=list[models.BucketReadNR], tags=['Buckets'])
def get_all_buckets(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    db_buckets = cruds.get_all_buckets(db=db, offset=offset, limit=limit)
    return db_buckets

@router.get("/bucket/{bucket_id}", response_model=models.BucketReadWR, tags=['Buckets'])
def get_bucket_by_id(bucket_id: int, db: SessionDep):
    
    db_bucket = cruds.get_bucket_by_id(db=db, bucket_id=bucket_id)
    if db_bucket is None:
        raise HTTPException(status_code=400, detail="Bucket does not exist")
    
    return db_bucket

@router.patch("/bucket/{bucket_id}", response_model=models.BucketReadWR, tags=['Buckets'])
def update_bucket(bucket_id: int, new_bucket: models.BucketUpdate, db: SessionDep):

    db_bucket = cruds.get_bucket_by_id(db=db, bucket_id=bucket_id)
    if db_bucket is None:
        raise HTTPException(status_code=400, detail="Bucket does not exist")
    
    return cruds.update_bucket_by_id(db=db, bucket_id=bucket_id, new_bucket=new_bucket)

@router.delete("/bucket/{bucket_id}", tags=['Buckets'])
def delete_bucket(bucket_id: int, db: SessionDep):
    
    db_bucket = cruds.get_bucket_by_id(db=db, bucket_id=bucket_id)
    if db_bucket is None:
        raise HTTPException(status_code=400, detail="Bucket does not exist")
    
    return cruds.delete_bucket_by_id(db=db, bucket_id=bucket_id)
