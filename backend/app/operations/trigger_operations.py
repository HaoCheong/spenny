from sqlalchemy.orm import Session
from datetime import datetime

import app.schemas.trigger_schemas as trigger_schemas
import app.schemas.bucket_schemas as bucket_schemas
import app.schemas.log_schemas as log_schemas

import app.cruds.bucket_cruds as bucket_cruds
import app.cruds.log_cruds as log_cruds

def solo_trigger(trigger: trigger_schemas.TriggerBase, db: Session):

    # Grab details of the a trigger
    if (trigger.from_bucket_id is not None):
        from_bucket = bucket_cruds.get_bucket_by_id(db=db, id=trigger.from_bucket_id)
        # update bucket value
        if (trigger.type == "SUB" or trigger.type == "MOV"):
            new_value = from_bucket["current_amount"] - trigger.change_amount
            new_bucket = bucket_schemas.BucketUpdate(current_amount=new_value)
            bucket_cruds.update_bucket_by_id(
                db=db, id=trigger.from_bucket_id, new_bucket=new_bucket)
            # create log
            new_log = log_schemas.LogCreate(
                name=trigger.name,
                description=trigger.description,
                type=trigger.type,
                amount=(trigger.change_amount) * -1,
                date_created=datetime.now(),
                bucket_id=trigger.from_bucket_id
            )
            log_cruds.create_log(db=db, log=new_log)

    if (trigger.to_bucket_id is not None):
        to_bucket = bucket_cruds.get_bucket_by_id(db=db, id=trigger.to_bucket_id)
        # update bucket value
        if (trigger.type == "ADD" or trigger.type == "MOV"):
            new_value = to_bucket["current_amount"] + trigger.change_amount
            new_bucket = bucket_schemas.BucketUpdate(current_amount=new_value)
            bucket_cruds.update_bucket_by_id(
                db=db, id=trigger.to_bucket_id, new_bucket=new_bucket)
            # create log
            new_log = log_schemas.LogCreate(
                name=trigger.name,
                description=trigger.description,
                type=trigger.type,
                amount=trigger.change_amount,
                date_created=datetime.now(),
                bucket_id=trigger.to_bucket_id
            )
            log_cruds.create_log(db=db, log=new_log)

    return {"Success": True}
