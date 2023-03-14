from typing import List

from helpers import get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import cruds
import schemas
import helpers

router = APIRouter()

# ======== BUCKET ENDPOINT ========


@router.post("/bucket", response_model=schemas.BucketReadNR, tags=['bucket'])
def create_bucket(bucket: schemas.BucketCreate, db: Session = Depends(get_db)):
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

# ======== FLOW EVENT ENDPOINT ========


@router.post("/flowEvent", response_model=schemas.FlowEventReadNR, tags=['flowEvent'])
def create_flowEvent(flowEvent: schemas.FlowEventCreate, db: Session = Depends(get_db)):
    return cruds.create_flowEvent(db=db, flowEvent=flowEvent)


@router.get("/flowEvents", response_model=List[schemas.FlowEventReadNR], tags=['flowEvent'])
def get_all_flowEvents(limit: int = 10, db: Session = Depends(get_db)):
    return cruds.get_all_flowEvents(db=db, limit=limit)


@router.get('/flowEvent/{flowEvent_id}', response_model=schemas.FlowEventReadWR, tags=['flowEvent'])
def get_flowEvent_by_id(flowEvent_id: int, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db=db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return db_flowEvent


@router.patch('/flowEvent/{flowEvent_id}', response_model=schemas.FlowEventReadWR, tags=['flowEvent'])
def update_flowEvent_by_id(flowEvent_id: int, new_flowEvent: schemas.FlowEventUpdate, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db=db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return cruds.update_flowEvent_by_id(db=db, id=flowEvent_id, new_flowEvent=new_flowEvent)


@router.delete('/flowEvent/{flowEvent_id}', tags=['flowEvent'])
def delete_flowEvent_by_id(flowEvent_id: int, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return cruds.delete_flowEvent_by_id(db, id=flowEvent_id)

# ======== LOG ENDPOINT ========


@router.post("/log", response_model=schemas.LogReadNR, tags=['log'])
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    return cruds.create_log(db=db, log=log)


@router.get("/logs", response_model=List[schemas.LogReadNR], tags=['log'])
def get_all_logs(limit: int = 10, db: Session = Depends(get_db)):
    return cruds.get_all_logs(db=db, limit=limit)


@router.get("/logs/{bucket_id}", response_model=List[schemas.LogReadNR], tags=['log'])
def get_all_logs_by_bucket_id(bucket_id: int, limit: int = 10, db: Session = Depends(get_db)):
    return cruds.get_all_logs_by_bucket_id(db=db, limit=limit, bucket_id=bucket_id)


@router.get('/log/{log_id}', response_model=schemas.LogReadWR, tags=['log'])
def get_log_by_id(log_id: int, db: Session = Depends(get_db)):
    db_log = cruds.get_log_by_id(db=db, id=log_id)
    if not db_log:
        raise HTTPException(status_code=400, detail="Log does not exist")

    return db_log


@router.patch('/log/{log_id}', response_model=schemas.LogReadWR, tags=['log'])
def update_log_by_id(log_id: int, new_log: schemas.LogUpdate, db: Session = Depends(get_db)):
    db_log = cruds.get_log_by_id(db=db, id=log_id)
    if not db_log:
        raise HTTPException(status_code=400, detail="Log does not exist")

    return cruds.update_log_by_id(db=db, id=log_id, new_log=new_log)


@router.delete('/log/{log_id}', tags=['log'])
def delete_log_by_id(log_id: int, db: Session = Depends(get_db)):
    db_log = cruds.get_log_by_id(db, id=log_id)
    if not db_log:
        raise HTTPException(status_code=400, detail="Log does not exist")

    return cruds.delete_log_by_id(db, id=log_id)
