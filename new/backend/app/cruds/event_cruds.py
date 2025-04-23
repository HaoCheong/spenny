''' Event CRUDs

Contains all the base functionailities for reading and writing event data into the database
5 base functionality:
- Create
- Read All instance
- Read an instance given an ID
- Update an instance given an ID
- Delete an instance given an ID

'''

from fastapi import HTTPException
from sqlmodel import Session, select

import app.models.event_models as models


def create_event(db: Session, new_event: models.EventCreate):
    
    db_event = models.Event.model_validate(new_event)

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event

def get_all_events(db: Session, offset: int = 0, limit: int = 100):
    event = db.exec(select(models.Event).offset(offset).limit(limit)).all()
    return event

def get_event_by_id(db: Session, event_id: int):

    event = db.get(models.Event, event_id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    return event

def update_event_by_id(db: Session, event_id: int, new_event: models.EventUpdate):
    event_db = db.get(models.Event, event_id)
    
    if not event_db:
        raise HTTPException(status_code=404, detail="Event not found")
    
    event_data = new_event.model_dump(exclude_unset=True)
    event_db.sqlmodel_update(event_data)

    db.add(event_db)
    db.commit()
    db.refresh(event_db)

    return event_db

def delete_event_by_id(db: Session, event_id: int):
    event = db.get(models.Event, event_id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    db.delete(event)
    db.commit()

    return {"Success": True}
