from app.helpers import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
import app.operations as op 

router = APIRouter()

@router.post("/api/v1/update", tags=["Admin"])
def run_update(update_datetime: datetime = datetime.now(timezone.utc), db: Session = Depends(get_db)):
    op.run_update(db=db, update_datetime=update_datetime)