from sqlalchemy.orm import Session
from sqlalchemy import and_, desc

import app.models.log_models as model
import app.schemas.log_schemas as schemas
from datetime import datetime



def create_log(db: Session, log: schemas.LogCreate, curr_datetime: datetime = datetime.now()):
    ''' Creating an new pet log '''

    db_log = model.Log(
        name=log.name,
        description=log.description,
        log_type=log.log_type,
        event_id=log.event_id,
        event_type=log.event_type,
        event_properties=log.event_properties,
        bucket_id=log.bucket_id,
        bucket_name=log.bucket_name,
        created_at=curr_datetime,
        updated_at=curr_datetime
    )

    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_all_logs(db: Session, skip: int = 0, limit: int = 100, all: bool = False):
    ''' Get every instance of pet log, using offset pagination '''
    query = db.query(model.Log)

    total = query.count()
    data = query.all() if all else query.order_by(model.Log.created_at.desc()).offset(skip).limit(limit).all()

    return schemas.LogAllRead.model_validate({
        "total": total,
        "data": data
    }, from_attributes=True)


def get_log_by_id(db: Session, id: int):
    ''' Get specific instance of log based on provided log ID '''
    return db.query(model.Log).filter(model.Log.id == id).first()


def get_all_logs_by_bucket_id(db: Session, bucket_id: int, skip: int = 0, limit: int = 100):
    ''' Get specific instance of log based on provided log ID '''
    query = db.query(model.Log).filter(model.Log.bucket_id == bucket_id)

    total = query.count()
    data = query.order_by(model.Log.created_at.desc()
                          ).offset(skip).limit(limit).all()

    return schemas.LogAllRead.model_validate({
        "total": total,
        "data": data
    }, from_attributes=True)


def get_all_logs_by_time_range(db: Session, start_date: datetime, end_date: datetime, int, skip: int = 0, limit: int = 100):
    ''' Get specific instance of log based on provided log ID '''
    query = db.query(model.Log).filter(
        and_(model.Log.created_at <= end_date, model.Log.created_at >= start_date))

    total = query.count()
    data = query.order_by(model.Log.created_at.desc()
                          ).offset(skip).limit(limit).all()

    return schemas.LogAllRead.model_validate({
        "total": total,
        "data": data
    }, from_attributes=True)


def delete_log_by_id(db: Session, id: int):
    ''' Delete specified instance of log on provided log ID '''
    db_log = db.query(model.Log).filter(model.Log.id == id).first()

    db.delete(db_log)
    db.commit()
    return {"Success": True}
