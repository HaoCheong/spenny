from app.helpers import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
import app.operations as op 
import app.domain.event.event_domain as schemas

router = APIRouter()

@router.post("/api/v1/update", tags=["Admin"])
def run_update(update_datetime: datetime = datetime.now(timezone.utc), db: Session = Depends(get_db)):
    op.run_update(db=db, update_datetime=update_datetime)
    return {"success": True}

# PFIX: Schema should NOT be event create, event has a very specific context that should not be violated
@router.post("/api/v1/trigger", tags=["Admin"])
def run_manual_entry(entry: schemas.EventCreate, db: Session = Depends(get_db)):
    op.run_manual_entry(db=db, entry=entry)
    return {"success": True}