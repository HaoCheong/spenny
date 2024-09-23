from typing import List

from app.utils.helpers import get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import app.api.schemas.flow_event_schemas as schemas
import app.api.cruds.flow_event_cruds as cruds

router = APIRouter()

# ======== FLOW EVENT ENDPOINT ========


@router.post("/flowEvent", response_model=schemas.FlowEventReadNR, tags=['Flow Event'])
def create_flowEvent(flowEvent: schemas.FlowEventCreate, db: Session = Depends(get_db)):
    return cruds.create_flowEvent(db=db, flowEvent=flowEvent)


@router.get("/flowEvents", response_model=List[schemas.FlowEventReadNR], tags=['Flow Event'])
def get_all_flowEvents(limit: int = 50, db: Session = Depends(get_db)):
    return cruds.get_all_flowEvents(db=db, limit=limit)


@router.get('/flowEvent/{flowEvent_id}', response_model=schemas.FlowEventReadWR, tags=['Flow Event'])
def get_flowEvent_by_id(flowEvent_id: int, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db=db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return db_flowEvent


@router.patch('/flowEvent/{flowEvent_id}', response_model=schemas.FlowEventReadWR, tags=['Flow Event'])
def update_flowEvent_by_id(flowEvent_id: int, new_flowEvent: schemas.FlowEventUpdate, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db=db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return cruds.update_flowEvent_by_id(db=db, id=flowEvent_id, new_flowEvent=new_flowEvent)


@router.delete('/flowEvent/{flowEvent_id}', tags=['Flow Event'])
def delete_flowEvent_by_id(flowEvent_id: int, db: Session = Depends(get_db)):
    db_flowEvent = cruds.get_flowEvent_by_id(db, id=flowEvent_id)
    if not db_flowEvent:
        raise HTTPException(status_code=400, detail="FlowEvent does not exist")

    return cruds.delete_flowEvent_by_id(db, id=flowEvent_id)
