from sqlalchemy.orm import Session

import app.models.log_models as model
import app.schemas.log_schemas as schemas


def create_log(db: Session, log: schemas.LogCreate):
    ''' Creating an new pet log '''
    
    db_log = model.Log(
        name=log.name,
        description=log.description,
        event_id=log.event_id,
        event_type=log.event_type,
        event_properties=log.event_properties,
        bucket_id=log.bucket_id,
        bucket_name=log.bucket_name,
        created_at=log.created_at,
        updated_at=log.updated_at
    )

    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_all_logs(db: Session, skip: int = 0, limit: int = 100):
    ''' Get every instance of pet log, using offset pagination '''
    total = db.query(model.Log).count()
    data = db.query(model.Log).offset(skip).limit(limit).all()
    return {
        "total": total,
        "data": data
    }


def get_log_by_id(db: Session, id: str):
    ''' Get specific instance of log based on provided log ID '''
    return db.query(model.Log).filter(model.Log.id == id).first()

def delete_log_by_id(db: Session, id: int):
    ''' Delete specified instance of log on provided log ID '''
    db_log = db.query(model.Log).filter(model.Log.id == id).first()

    db.delete(db_log)
    db.commit()
    return {"Success": True}
