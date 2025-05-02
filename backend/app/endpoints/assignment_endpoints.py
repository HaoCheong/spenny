import app.cruds.assignment_cruds as assignment_cruds
import app.cruds.event_cruds as event_cruds
import app.cruds.bucket_cruds as bucket_cruds
from typing import List

from app.helpers import get_db
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

router = APIRouter()


# ======== ASSIGNING EVENTS TO BUCKET ========


@router.post("/api/v1/assignToBucket/{event_id}/{bucket_id}", tags=["Bucket Event Assignment"])
def assign_event_to_bucket(event_id: int, bucket_id: int, db: Session = Depends(get_db)):
    db_bucket = bucket_cruds.get_bucket_by_id(db, id=bucket_id)
    db_event = event_cruds.get_event_by_id(db, id=event_id)

    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    if db_event in db_bucket.events:
        raise HTTPException(
            status_code=400, detail="Event already assigned to bucket")

    return assignment_cruds.assign_event_to_bucket(db, event_id=event_id, bucket_id=bucket_id)


@router.post("/api/v1/unassignFromBucket/{event_id}/{bucket_id}", tags=["Bucket Event Assignment"])
def unassign_event_from_bucket(event_id: int, bucket_id: int, db: Session = Depends(get_db)):
    db_bucket = bucket_cruds.get_bucket_by_id(db, id=bucket_id)
    db_event = event_cruds.get_event_by_id(db, id=event_id)

    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    if db_event not in db_bucket.events:
        raise HTTPException(
            status_code=400, detail="Event not assigned to bucket")

    return assignment_cruds.unassign_event_from_bucket(db, event_id=event_id, bucket_id=bucket_id)
