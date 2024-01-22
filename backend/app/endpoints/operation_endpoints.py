from app.helpers import get_db
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

import app.schemas.trigger_schemas as schemas
import app.operations.bucket_operations as bucket_operations
import app.operations.trigger_operations as trigger_operations
import app.cruds.bucket_cruds as bucket_cruds


router = APIRouter()

# ========== OPERATION =========

# When trigger it will run this application and update all the flow amount to the current date
@router.put('/updateValues', tags=['Operations'])
def update_all_buckets(db: Session = Depends(get_db)):
    return bucket_operations.update_all_buckets(db=db)


@router.put('/soloTrigger', tags=['Operations'])
def solo_trigger(trigger: schemas.TriggerBase, db: Session = Depends(get_db)):
    return trigger_operations.solo_trigger(trigger=trigger, db=db)

# ========== TEST ==========
# A test endpoint to easily test our certain functions via swagger
@router.get('/TEST')
def test(db: Session = Depends(get_db)):
    return bucket_cruds.get_bucket_flowEvents(bucket_id=1, db=db)
