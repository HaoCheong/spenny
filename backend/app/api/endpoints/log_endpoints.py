from typing import List

from app.utils.helpers import get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import app.api.schemas.log_schemas as schemas
import app.api.cruds.log_cruds as cruds

router = APIRouter()

# ======== LOG ENDPOINT ========


@router.post("/log", response_model=schemas.LogReadNR, tags=['Log'])
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    return cruds.create_log(db=db, log=log)


@router.get("/logs", response_model=List[schemas.LogReadNR], tags=['Log'])
def get_all_logs(limit: int = 1000, db: Session = Depends(get_db)):
    return cruds.get_all_logs(db=db, limit=limit)


@router.get("/logs/{bucket_id}/{date}", response_model=List[schemas.LogReadNR], tags=['Log'])
def get_all_logs_by_bucket_id(bucket_id: int, date: str, db: Session = Depends(get_db)):
    return cruds.get_all_logs_by_bucket_id(db=db, date=date, bucket_id=bucket_id)


@router.get('/log/{log_id}', response_model=schemas.LogReadWR, tags=['Log'])
def get_log_by_id(log_id: int, db: Session = Depends(get_db)):
    db_log = cruds.get_log_by_id(db=db, id=log_id)
    if not db_log:
        raise HTTPException(status_code=400, detail="Log does not exist")

    return db_log


@router.patch('/log/{log_id}', response_model=schemas.LogReadWR, tags=['Log'])
def update_log_by_id(log_id: int, new_log: schemas.LogUpdate, db: Session = Depends(get_db)):
    db_log = cruds.get_log_by_id(db=db, id=log_id)
    if not db_log:
        raise HTTPException(status_code=400, detail="Log does not exist")

    return cruds.update_log_by_id(db=db, id=log_id, new_log=new_log)


@router.delete('/log/{log_id}', tags=['Log'])
def delete_log_by_id(log_id: int, db: Session = Depends(get_db)):
    db_log = cruds.get_log_by_id(db, id=log_id)
    if not db_log:
        raise HTTPException(status_code=400, detail="Log does not exist")

    return cruds.delete_log_by_id(db, id=log_id)
