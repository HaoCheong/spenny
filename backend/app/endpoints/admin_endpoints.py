from app.helpers import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
import app.operations as op 
import app.domain.event.event_domain as schemas
import app.cruds.bucket_cruds as bucket_cruds
router = APIRouter()

@router.post("/api/v1/update", tags=["Admin"])
def run_update(update_datetime: datetime = datetime.now(timezone.utc), db: Session = Depends(get_db)):
    
    op.run_update(db=db, update_datetime=update_datetime)
    return {"success": True}

@router.post("/api/v1/trigger", tags=["Admin"])
def run_manual_entry(entry: schemas.ManualActionBase, db: Session = Depends(get_db)):

    db_bucket = bucket_cruds.get_bucket_by_id(db=db, id=entry.bucket_id)
    if (not db_bucket):
        raise HTTPException(
            status_code=400, detail=f"Bucket with ID {entry.bucket_id} does not exists")
    
    op.run_manual_entry(db=db, entry=entry)
    return {"success": True}