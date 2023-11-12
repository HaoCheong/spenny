from sqlalchemy.orm import Session
import models
import schemas
import cruds
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from helpers import add_time

def solo_trigger(trigger: schemas.TriggerBase, db: Session):
    # Grab details of the a trigger
    if (trigger.from_bucket_id is not None):
        print("HERE 1", trigger)
        from_bucket = cruds.get_bucket_by_id(db=db, id=trigger.from_bucket_id)
        # update bucket value
        if (trigger.type == "SUB" or trigger.type == "MOV"):
            new_value = from_bucket["current_amount"] - trigger.change_amount
            print("FROM NEW VALUE", new_value)
            new_bucket = schemas.BucketUpdate(current_amount=new_value)
            cruds.update_bucket_by_id(
                db=db, id=trigger.from_bucket_id, new_bucket=new_bucket)
            # create log
            new_log = schemas.LogCreate(
                name=trigger.name,
                description=trigger.description,
                type=trigger.type,
                amount=(trigger.change_amount) * -1,
                date_created=datetime.now(),
                bucket_id=trigger.from_bucket_id
            )
            cruds.create_log(db=db, log=new_log)

    if (trigger.to_bucket_id is not None):
        to_bucket = cruds.get_bucket_by_id(db=db, id=trigger.to_bucket_id)
        # update bucket value
        if (trigger.type == "ADD" or trigger.type == "MOV"):
            new_value = to_bucket["current_amount"] + trigger.change_amount
            print("TO NEW VALUE", new_value)
            new_bucket = schemas.BucketUpdate(current_amount=new_value)
            cruds.update_bucket_by_id(
                db=db, id=trigger.to_bucket_id, new_bucket=new_bucket)
            # create log
            new_log = schemas.LogCreate(
                name=trigger.name,
                description=trigger.description,
                type=trigger.type,
                amount=trigger.change_amount,
                date_created=datetime.now(),
                bucket_id=trigger.to_bucket_id
            )
            cruds.create_log(db=db, log=new_log)

    return {"SUccess": True}
