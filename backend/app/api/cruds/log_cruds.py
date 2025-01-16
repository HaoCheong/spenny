from datetime import datetime

import app.api.models.log_model as models
import app.api.schemas.log_schemas as schemas
from sqlalchemy.orm import Session

# ======== LOG ========

def create_log(db: Session, log: schemas.LogCreate):
    db_log = models.Log(
        name=log.name,
        description=log.description,
        amount=log.amount,
        type=log.type,
        date_created=log.date_created,
        bucket_id=log.bucket_id
    )

    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_all_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Log).offset(skip).limit(limit).all()

# Get all the logs for a bucket after a specified date


def get_all_logs_by_bucket_id(db: Session, bucket_id: int, date: str):
    cap_date = datetime.strptime(date, "%d-%m-%Y")
    return db.query(models.Log).filter(models.Log.bucket_id == bucket_id).filter(models.Log.date_created > cap_date).order_by(models.Log.date_created).all()


def get_log_by_id(db: Session, id: int):
    return db.query(models.Log).filter(models.Log.id == id).first()


def update_log_by_id(db: Session, id: int, new_log: schemas.LogUpdate):
    db_log = db.query(models.Log).filter(
        models.Log.id == id).first()

    # Converts new_owner from model.object to dictionary
    update_log = new_log.dict(exclude_unset=True)

    # Loops through dictionary and update db_owner
    for key, value in update_log.items():
        setattr(db_log, key, value)

    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def delete_log_by_id(db: Session, id: int):
    db_log = db.query(models.Log).filter(
        models.Log.id == id).first()

    db.delete(db_log)
    db.commit()
    return {"Success": True}
