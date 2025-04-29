
import app.cruds.event_cruds as event_cruds
import app.cruds.bucket_event_assignment_cruds as bucket_event_assignment_cruds
import app.cruds.bucket_cruds as bucket_cruds
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database.database import get_session

router = APIRouter()


@router.post("/assignToBucket/{event_id}/{bucket_id}", tags=["Event Bucket Assignment"])
def assign_event_to_bucket(event_id: int, bucket_id: int, db: Session = Depends(get_session)):
    db_bucket = bucket_cruds.get_bucket_by_id(db, bucket_id=bucket_id)
    db_event = event_cruds.get_event_by_id(db, event_id=event_id)

    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    if db_event in db_bucket.events:
        raise HTTPException(
            status_code=400, detail="Event already assigned to bucket")

    return bucket_event_assignment_cruds.assign_event_to_bucket(db, event_id=event_id, bucket_id=bucket_id)


@router.post("/unassignFromBucket/{event_id}/{bucket_id}", tags=["Event Bucket Assignment"])
def unassign_event_from_bucket(event_id: int, bucket_id: int, db: Session = Depends(get_session)):
    db_bucket = bucket_cruds.get_bucket_by_id(db, bucket_id=bucket_id)
    db_event = event_cruds.get_event_by_id(db, event_id=event_id)

    if not db_bucket:
        raise HTTPException(status_code=400, detail="Bucket does not exist")

    if not db_event:
        raise HTTPException(status_code=400, detail="Event does not exist")

    if db_event not in db_bucket.events:
        raise HTTPException(
            status_code=400, detail="Event not assigned to bucket")

    return bucket_event_assignment_cruds.unassign_event_from_bucket(db, event_id=event_id, bucket_id=bucket_id)
