from typing import List

from app.helpers import get_db
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import app.schemas.log_schemas as schemas
import app.cruds.log_cruds as cruds
import app.operations.event_operations as event_op

router = APIRouter()


@router.post("/api/v1/log", response_model=schemas.LogCreate, tags=["Logs"])
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    event_op.EventOperation.update_all_events(db=db)
    return cruds.create_log(db=db, log=log)


@router.get("/api/v1/logs", response_model=schemas.LogAllRead, tags=["Logs"])
def get_all_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    event_op.EventOperation.update_all_events(db=db)
    db_log_data = cruds.get_all_logs(db, skip, limit)
    return db_log_data


@router.get("/api/v1/logs/{bucket_id}", response_model=schemas.LogAllRead, tags=["Logs"])
def get_all_logs_by_bucket_id(bucket_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    event_op.EventOperation.update_all_events(db=db)
    db_log_data = cruds.get_all_logs_by_bucket_id(
        bucket_id=bucket_id, db=db, skip=skip, limit=limit)
    return db_log_data


@router.post("/api/v1/logs/time_range", response_model=schemas.LogAllRead, tags=["Logs"])
def get_all_logs_by_time_range(time_range: schemas.LogTimeRange, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    event_op.EventOperation.update_all_events(db=db)
    db_log_data = cruds.get_all_logs_by_time_range(
        start_date=time_range.start_date, end_date=time_range.end_data, db=db, skip=skip, limit=limit)
    return db_log_data


@router.get("/api/v1/log/{log_id}", response_model=schemas.LogRead, tags=["Logs"])
def get_log_by_id(log_id: int, db: Session = Depends(get_db)):
    event_op.EventOperation.update_all_events(db=db)
    db_log = cruds.get_log_by_id(db, id=log_id)
    if not db_log:
        raise HTTPException(status_code=400, detail="Log does not exist")

    return db_log


@router.delete("/api/v1/log/{log_id}", tags=["Logs"])
def delete_log_by_id(log_id: int, db: Session = Depends(get_db)):
    db_log = cruds.get_log_by_id(db, id=log_id)
    if not db_log:
        raise HTTPException(status_code=400, detail="Log does not exist")

    return cruds.delete_log_by_id(db, id=log_id)
