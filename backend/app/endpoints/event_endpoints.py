from typing import List

from app.helpers import get_db
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import app.schemas.event_schemas as schemas
import app.cruds.event_cruds as event_cruds
import app.cruds.bucket_cruds as bucket_cruds

# import app.operations.event_operations as event_op
router = APIRouter()


@router.post("/api/v1/event", response_model=schemas.EventReadNR, tags=["Events"])
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):

    db_bucket = bucket_cruds.get_bucket_by_id(db=db, id=event.bucket_id)
    if not db_bucket:
        raise HTTPException(
            status_code=400, detail="Bucket to be assigned does not exist")

    res = event_cruds.create_event(db=db, event=event)

    return res


@router.get("/api/v1/events", response_model=schemas.EventAllRead, tags=["Events"])
def get_all_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)
    db_events = event_cruds.get_all_events(db, skip, limit)
    return db_events


@router.get("/api/v1/event/{event_id}", response_model=schemas.EventReadWR, tags=["Events"])
def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)
    db_event = event_cruds.get_event_by_id(db, id=event_id)
    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    return db_event


@router.post("/api/v1/event/trigger/{event_id}", response_model=schemas.EventReadWR, tags=["Events"])
def trigger_event():
    return {"status": "Code Incomplete"}

@router.post("/api/v1/event/entry", tags=["Events"])
def event_entry():
    return {"status": "Code Incomplete"}

@router.post("/api/v1/event/timeframe", response_model=schemas.EventAllRead, tags=["Events"])
def get_all_event_by_timeframe():
    pass

@router.patch("/api/v1/event/{event_id}", response_model=schemas.EventReadNR, tags=["Events"])
def update_event_by_id(event_id: int, new_event: schemas.EventUpdate, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)
    db_event = event_cruds.get_event_by_id(db, id=event_id)
    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    return event_cruds.update_event_by_id(db, id=event_id, new_event=new_event)


@router.delete("/api/v1/event/{event_id}", tags=["Events"])
def delete_event_by_id(event_id: int, db: Session = Depends(get_db)):
    # event_op.EventOperation.update_all_events(db=db)
    db_event = event_cruds.get_event_by_id(db, id=event_id)
    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    return event_cruds.delete_event_by_id(db, id=event_id)
