from typing import List

from app.helpers import get_db
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import app.schemas.log_schemas as schemas
import app.cruds.log_cruds as cruds

router = APIRouter()


@router.post("/api/v1/log", response_model=schemas.LogCreate, tags=["Logs"])
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    return cruds.create_log(db=db, log=log)


@router.get("/api/v1/logs", response_model=schemas.LogAllRead, tags=["Logs"])
def get_all_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_log_data = cruds.get_all_logs(db, skip, limit)
    return db_log_data


@router.get("/api/v1/log/{log_id}", response_model=schemas.LogRead, tags=["Logs"])
def get_log_by_id(log_id: int, db: Session = Depends(get_db)):
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
