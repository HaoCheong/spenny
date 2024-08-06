from typing import List

from app.helpers import get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import app.schemas.flow_event_schemas as schemas
import app.cruds.flow_event_cruds as cruds

router = APIRouter()

# ======== FLOW EVENT ENDPOINT ========


@router.post("/api/v1/flowEvent", response_model=schemas.FlowEventReadNR, tags=['Flow Event'])
def create_flowEvent(flowEvent: schemas.FlowEventCreate, db: Session = Depends(get_db)):
    return cruds.create_flowEvent(db=db, flowEvent=flowEvent)


@router.get("/api/v1/flowEvents", response_model=List[schemas.FlowEventReadNR], tags=['Flow Event'])
def get_all_flowEvents(limit: int = 50, db: Session = Depends(get_db)):
    return cruds.get_all_flowEvents(db=db, limit=limit)


@router.get('/api/v1/flowEvent/{flowEvent_id}', response_model=schemas.FlowEventReadWR, tags=['Flow Event'])
def get_flowEvent_by_id(flowEvent_id: int, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db=db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return db_flowEvent


@router.patch('/api/v1/flowEvent/{flowEvent_id}', response_model=schemas.FlowEventReadWR, tags=['Flow Event'])
def update_flowEvent_by_id(flowEvent_id: int, new_flowEvent: schemas.FlowEventUpdate, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db=db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return cruds.update_flowEvent_by_id(db=db, id=flowEvent_id, new_flowEvent=new_flowEvent)


@router.delete('/api/v1/flowEvent/{flowEvent_id}', tags=['Flow Event'])
def delete_flowEvent_by_id(flowEvent_id: int, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return cruds.delete_flowEvent_by_id(db, id=flowEvent_id)
