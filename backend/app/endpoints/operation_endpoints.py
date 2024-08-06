from app.helpers import get_db
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

import app.schemas.trigger_schemas as schemas
import app.operations.bucket_operations as bucket_operations
import app.operations.trigger_operations as trigger_operations
import app.cruds.bucket_cruds as bucket_cruds
import app.cruds.flow_event_cruds as flow_event_cruds


router = APIRouter()

# ========== OPERATION =========

# When trigger it will run this application and update all the flow amount to the current date


@router.put('/api/v1/updateValues', tags=['Operations'])
def update_all_buckets(db: Session = Depends(get_db)):
    return bucket_operations.update_all_buckets(db=db)


# @router.put('/api/v1/soloTrigger', tags=['Operations'])
# def solo_trigger(trigger: schemas.TriggerBase, db: Session = Depends(get_db)):
#     return trigger_operations.solo_trigger(trigger=trigger, db=db)


@router.put('/api/v1/manualTrigger', tags=['Operations'])
def manual_trigger(trigger: schemas.TriggerBase, db: Session = Depends(get_db)):
    return trigger_operations.manual_trigger(trigger=trigger, db=db)


# @router.put('/api/v1/bringForward', tags=['Operations'])
# def bring_forward(details: schemas.BringForwardBase, db: Session = Depends(get_db)):

#     db_flowEvent = flow_event_cruds.get_flowEvent_by_id(
#         db, id=details.flow_event_id)
#     if not db_flowEvent:
#         raise HTTPException(
#             status_code=400, detail="Flow Event does not exist")

#     return trigger_operations.bringForward(details=details, db=db)

@router.put('/api/v1/bringForward', tags=['Operations'])
def bring_forward(details: schemas.BringForwardBase, db: Session = Depends(get_db)):

    db_flowEvent = flow_event_cruds.get_flowEvent_by_id(
        db, id=details.flow_event_id)

    if not db_flowEvent:
        raise HTTPException(
            status_code=400, detail="Flow Event does not exist")

    return trigger_operations.bring_forward(details=details, db=db)

# ========== TEST ==========
# A test endpoint to easily test our certain functions via swagger


@router.put('/api/v1/manualTrigger', tags=['Operations'])
def manual_trigger(trigger: schemas.TriggerBase, db: Session = Depends(get_db)):
    # Verify that both of the trigger buckets are not None
    if trigger.from_bucket_id is None and trigger.to_bucket_id is None:
        raise HTTPException(
            status_code=400, detail="From and To bucket IDs are both None")

    # Verify that both trigger buckets exist
    db_from_bucket = bucket_cruds.get_bucket_by_id(
        db=db, id=trigger.from_bucket_id)
    db_to_bucket = bucket_cruds.get_bucket_by_id(
        db=db, id=trigger.to_bucket_id)

    if trigger.from_bucket_id is not None and db_from_bucket is None:
        raise HTTPException(
            status_code=404, detail="Requested From bucket does not exist")

    if trigger.to_bucket_id is not None and db_to_bucket is None:
        raise HTTPException(
            status_code=404, detail="Requested To bucket does not exist")

    return trigger_operations.solo_trigger(trigger=trigger, db=db)


@router.get('/TEST')
def test(db: Session = Depends(get_db)):
    return bucket_cruds.get_bucket_flowEvents(bucket_id=1, db=db)
