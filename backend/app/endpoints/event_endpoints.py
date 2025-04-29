''' Nutrition Plan Endpoints

Contains all the function that subsequently call the nutrition plan CRUD functions (see CRUD files)
Split was done because it allowed for simplified data validation and db calling.
- Endpoints: Takes in and validates input correctness
- CRUD: Focused on the logic of formatting and manipulating data, under the assumption that the provided data was correct

'''

from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

import app.cruds.event_cruds as cruds
import app.models.event_models as models
from app.database.database import SessionDep

router = APIRouter()

@router.post("/event/", response_model=models.EventReadNR, tags=['Events'])
def create_event(event: models.EventCreate, db: SessionDep):
    db_event = cruds.create_event(db=db, new_event=event)
    return db_event

@router.get("/events/", response_model=list[models.EventReadNR], tags=['Events'])
def get_all_events(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    db_events = cruds.get_all_events(db=db, offset=offset, limit=limit)
    return db_events

@router.get("/event/{event_id}", response_model=models.EventReadWR, tags=['Events'])
def get_event_by_id(event_id: int, db: SessionDep):
    
    db_event = cruds.get_event_by_id(db=db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=400, detail="Event does not exist")
    
    return db_event

@router.patch("/event/{event_id}", response_model=models.EventReadWR, tags=['Events'])
def update_event(event_id: int, new_event: models.EventUpdate, db: SessionDep):

    db_event = cruds.get_event_by_id(db=db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=400, detail="Event does not exist")
    
    return cruds.update_event_by_id(db=db, event_id=event_id, new_event=new_event)

@router.delete("/event/{event_id}", tags=['Events'])
def delete_event(event_id: int, db: SessionDep):
    
    db_event = cruds.get_event_by_id(db=db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=400, detail="Event does not exist")
    
    return cruds.delete_event_by_id(db=db, event_id=event_id)
