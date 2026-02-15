from sqlalchemy.orm import Session
from datetime import datetime
import app.models.event_models as model
import app.schemas.event_schemas as schemas


def create_event(db: Session, event: schemas.EventCreate, curr_datetime: datetime = datetime.now()):
    ''' Creating an new pet event '''

    # event = schemas.EventUnion.model_validate(event)

    db_event = model.Event(
        name=event.name,
        description=event.description,
        trigger=event.trigger.model_dump(mode="json"),
        operation=event.operation.model_dump(mode="json"),
        bucket_id=event.bucket_id,
        created_at=curr_datetime,
        updated_at=curr_datetime
    )

    print("CREATE_EVENT HERE 1", event.trigger.model_dump())
    print("CREATE_EVENT HERE 2", event.operation.model_dump())

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def get_all_events(db: Session, skip: int = 0, limit: int = 100, all: bool = False) -> schemas.EventAllRead:
    ''' Get every instance of pet event, using offset pagination '''

    query = db.query(model.Event).order_by(model.Event.id)

    total = query.count()
    data = query.all() if all else query.offset(skip).limit(limit).all()

    return schemas.EventAllRead.model_validate({
        "total": total,
        "data": data
    }, from_attributes=True)


def get_event_by_id(db: Session, id: int):
    ''' Get specific instance of event based on provided event ID '''
    db_event = db.query(model.Event).filter(model.Event.id == id).first()
    return db_event


def get_next_event(db: Session):
    ''' Get specific instance of event based that is next to run '''

    db_event = db.query(model.Event).order_by(
        model.Event.trigger_datetime).limit(1).first()
    return db_event


def get_all_event_by_timeframe(db: Session, first_date: datetime = None, last_date: datetime = datetime.now(), skip: int = 0, limit: int = 0, all: bool = False) -> schemas.EventAllRead:

    query = None
    if first_date is None:
        query = db.query(model.Event).filter(
            model.Event.trigger_datetime < last_date)
    else:
        query = db.query(model.Event).filter(
            model.Event.trigger_datetime < last_date, model.Event.trigger_datetime > first_date)

    total = query.count()
    db_events = query.all() if all is True else query.offset(skip).limit(limit).all()

    return schemas.EventAllRead.model_validate({
        "total": total,
        "data": db_events
    }, from_attributes=True)


def update_event_by_id(db: Session, id: int, new_event: schemas.EventUpdate, update_time: datetime = datetime.now()):
    ''' Update specific fields of specified instance of event on provided event ID '''
    db_event = db.query(model.Event).filter(model.Event.id == id).first()

    # Converts new_event from model object to dictionary
    update_event = new_event.dict(exclude_unset=True)

    # Loops through dictionary and update db_event
    for key, value in update_event.items():
        setattr(db_event, key, value)

    setattr(db_event, "updated_at", update_time)

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
