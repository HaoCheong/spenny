
from sqlmodel import Session

import app.models.event_models as event_models
import app.models.bucket_models as bucket_models


def assign_event_to_bucket(db: Session, bucket_id: int, event_id: int):
    ''' Assign instance of pet to an nutrition plan. One to One Relationship '''
    # Getting both instance of Pet and Nutrition Plan
    db_bucket = db.get(bucket_models.Bucket, bucket_id)
    db_event = db.get(event_models.Event, event_id)

    # Establish the relationship
    db_bucket.events.append(db_event)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_bucket)
    db.commit()
    return {"Success": True}


def unassign_event_from_bucket(db: Session, bucket_id: int, event_id: int):
    ''' Unassign instance of pet to an nutrition plan '''

    # Getting both instance of Pet and Nutrition Plan
    db_bucket = db.get(bucket_models.Bucket, bucket_id)
    db_event = db.get(event_models.Event, event_id)

    # Clear their relationship
    db_bucket.events.remove(db_event)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_bucket)
    db.commit()

    return {"Success": True}
