from sqlalchemy.orm import Session

import app.models.bucket_models as bucket_models
import app.models.event_models as event_models


def assign_event_to_bucket(db: Session, event_id: int, bucket_id: int):
    ''' Assign instance of event to an bucket. Many to One Relationship '''

    # Getting both instance of Event and Bucket
    db_event = db.query(event_models.Event).filter(
        event_models.Event.id == event_id).first()
    db_bucket = db.query(bucket_models.Bucket).filter(
        bucket_models.Bucket.id == bucket_id).first()

    # Treat adding relation like adding to event bucket's events list
    db_bucket.events.append(db_event)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_bucket)
    db.commit()

    return {"Success", True}


def unassign_event_from_bucket(db: Session, event_id: int, bucket_id: int):
    ''' Unassign instance of event to an bucket '''

    # Getting both instance of Event and Bucket
    db_event = db.query(event_models.Event).filter(
        event_models.Event.id == event_id).first()
    db_bucket = db.query(bucket_models.Bucket).filter(
        bucket_models.Bucket.id == bucket_id).first()

    # Treat removing relation like removing from event bucket's events list
    db_bucket.events.remove(db_event)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_bucket)
    db.commit()

    return {"Success", True}