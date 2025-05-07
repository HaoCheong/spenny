from sqlalchemy.orm import Session

import app.models.event_models as model
import app.schemas.event_schemas as schemas


def create_event(db: Session, event: schemas.EventCreate):
    ''' Creating an new pet event '''

    # event = schemas.EventUnion.model_validate(event)

    db_event = model.Event(
        name=event.name,
        description=event.description,
        trigger_datetime=event.trigger_datetime,
        frequency=event.frequency,
        event_type=event.event_type,
        properties=event.properties.model_dump(),
        created_at=event.created_at,
        updated_at=event.updated_at
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_all_events(db: Session, skip: int = 0, limit: int = 100):
    ''' Get every instance of pet event, using offset pagination '''

    query = db.query(model.Event)

    total = query.count()
    data = query.offset(skip).limit(limit).all()

    return {
        "total": total,
        "data": data
    }


def get_event_by_id(db: Session, id: str):
    ''' Get specific instance of event based on provided event ID '''
    return db.query(model.Event).filter(model.Event.id == id).first()


def update_event_by_id(db: Session, id: int, new_event: schemas.EventUpdate):
    ''' Update specific fields of specified instance of event on provided event ID '''
    db_event = db.query(model.Event).filter(model.Event.id == id).first()

    # Converts new_event from model object to dictionary
    update_event = new_event.dict(exclude_unset=True)

    # Loops through dictionary and update db_event
    for key, value in update_event.items():
        setattr(db_event, key, value)

    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def delete_event_by_id(db: Session, id: int):
    ''' Delete specified instance of event on provided event ID '''
    db_event = db.query(model.Event).filter(model.Event.id == id).first()

    db.delete(db_event)
    db.commit()
    return {"Success": True}
