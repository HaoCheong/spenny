from typing import List

from app.helpers import get_db
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import app.schemas.event_schemas as schemas
import app.cruds.event_cruds as cruds

router = APIRouter()


@router.post("/api/v1/event", response_model=schemas.EventReadNR, tags=["Events"])
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return cruds.create_event(db=db, event=event)


@router.get("/api/v1/events", response_model=List[schemas.EventReadNR], tags=["Events"])
def get_all_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_events = cruds.get_all_events(db, skip, limit)
    return db_events


@router.get("/api/v1/event/{event_id}", response_model=schemas.EventReadWR, tags=["Events"])
def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    db_event = cruds.get_event_by_id(db, id=event_id)
    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    return db_event


@router.patch("/api/v1/event/{event_id}", response_model=schemas.EventReadNR, tags=["Events"])
def update_event_by_id(event_id: int, new_event: schemas.EventUpdate, db: Session = Depends(get_db)):
    db_event = cruds.get_event_by_id(db, id=event_id)
    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    return cruds.update_event_by_id(db, id=event_id, new_event=new_event)


@router.delete("/api/v1/event/{event_id}", tags=["Events"])
def delete_event_by_id(event_id: int, db: Session = Depends(get_db)):
    db_event = cruds.get_event_by_id(db, id=event_id)
    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    return cruds.delete_event_by_id(db, id=event_id)
