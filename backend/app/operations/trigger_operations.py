from datetime import datetime
from typing import Dict

from fastapi import HTTPException

import app.api.schemas.trigger_schemas as trigger_schemas
import app.api.schemas.bucket_schemas as bucket_schemas
import app.api.schemas.log_schemas as log_schemas
import app.api.schemas.flow_event_schemas as flow_event_schemas

import app.api.cruds.bucket_cruds as bucket_cruds
import app.api.cruds.log_cruds as log_cruds
import app.api.cruds.flow_event_cruds as flow_event_cruds

from app.utils.helpers import add_time
from app.operations.operation_helpers import change_bucket_value


# def solo_trigger(trigger: trigger_schemas.TriggerBase, db: Session):

#     trigger = jsonable_encoder(trigger)

#     # Grab details of the a trigger
#     if (trigger["from_bucket_id"] is not None):

#         from_bucket = jsonable_encoder(
#             bucket_cruds.get_bucket_by_id(db=db, id=trigger["from_bucket_id"]))

#         # update bucket value
#         if (trigger["type"] == "SUB" or trigger["type"] == "MOV"):

#             new_value = round(
#                 from_bucket["current_amount"] - trigger["change_amount"], 2)
#             new_bucket = bucket_schemas.BucketUpdate(current_amount=new_value)

#             bucket_cruds.update_bucket_by_id(
#                 db=db, id=trigger["from_bucket_id"], new_bucket=new_bucket)
#             # create log

#             new_log = log_schemas.LogCreate(
#                 name=trigger["name"],
#                 description=trigger["description"],
#                 type=trigger["type"],
#                 amount=(trigger["change_amount"]) * -1,
#                 date_created=datetime.now(),
#                 bucket_id=trigger["from_bucket_id"]
#             )
#             log_cruds.create_log(db=db, log=new_log)

#     if (trigger["to_bucket_id"] is not None):
#         to_bucket = jsonable_encoder(
#             bucket_cruds.get_bucket_by_id(db=db, id=trigger["to_bucket_id"]))
#         # update bucket value
#         if (trigger["type"] == "ADD" or trigger["type"] == "MOV"):
#             new_value = round(
#                 to_bucket["current_amount"] + trigger["change_amount"], 2)
#             new_bucket = bucket_schemas.BucketUpdate(current_amount=new_value)
#             bucket_cruds.update_bucket_by_id(
#                 db=db, id=trigger["to_bucket_id"], new_bucket=new_bucket)
#             # create log
#             new_log = log_schemas.LogCreate(
#                 name=trigger["name"],
#                 description=trigger["description"],
#                 type=trigger["type"],
#                 amount=trigger["change_amount"],
#                 date_created=datetime.now(),
#                 bucket_id=trigger["to_bucket_id"]
#             )
#             log_cruds.create_log(db=db, log=new_log)

#     return {"Success": True}

# # I fucking hate this function, do better


# def bringForward(details: trigger_schemas.BringForwardBase, db: Session):

#     db_flow_event = flow_event_cruds.get_flowEvent_by_id(
#         db=db, id=details.flow_event_id)

#     if (details.money_include):
#         trigger_details = {
#             "name": f"Bring Forward - {db_flow_event.name}",
#             "description": f"Bring Forward - {db_flow_event.description}",
#             "change_amount": db_flow_event.change_amount,
#             "type": db_flow_event.type,
#             "from_bucket_id": db_flow_event.from_bucket_id,
#             "to_bucket_id": db_flow_event.to_bucket_id
#         }

#         solo_trigger(trigger_details, db)

#         new_date = add_time(db_flow_event.next_trigger,
#                             db_flow_event.frequency)
#         res = flow_event_cruds.update_flowEvent_by_id(
#             db=db,
#             id=db_flow_event.id,
#             new_flowEvent=flow_event_schemas.FlowEventUpdate(
#                 next_trigger=new_date)
#         )

#         return {"Success": True}
#     else:
#         # Update just date
#         new_date = add_time(db_flow_event.next_trigger,
#                             db_flow_event.frequency)
#         res = flow_event_cruds.update_flowEvent_by_id(
#             db=db,
#             id=db_flow_event.id,
#             new_flowEvent=flow_event_schemas.FlowEventUpdate(
#                 next_trigger=new_date)
#         )

#         return {"Success": True}


def manual_trigger(trigger: trigger_schemas.TriggerBase, db: Session, date_triggered: datetime = datetime.now()) -> Dict:
    '''
    Manual triggers an event for one or more buckets. Such as Add, Sub, Move 
    '''

    trigger = jsonable_encoder(trigger)

    db_from_bucket = jsonable_encoder(
        bucket_cruds.get_bucket_by_id(db=db, id=trigger["from_bucket_id"]))

    db_to_bucket = jsonable_encoder(
        bucket_cruds.get_bucket_by_id(db=db, id=trigger["to_bucket_id"]))

    if trigger["type"] == "ADD":

        # Adds values from the TO BUCKET
        change_bucket_value(db_to_bucket, 'ADD', trigger["change_amount"], db)

        new_log = log_schemas.LogCreate(
            name=trigger["name"],
            description=trigger["description"],
            type=trigger["type"],
            amount=(trigger["change_amount"]) * -1,
            date_created=date_triggered,
            bucket_id=trigger["to_bucket_id"]
        )
        log_cruds.create_log(db=db, log=new_log)

    elif trigger["type"] == "SUB":

        # Subtracts values from the FROM BUCKET
        change_bucket_value(db_from_bucket, 'SUB',
                            trigger["change_amount"], db)

        new_log = log_schemas.LogCreate(
            name=trigger["name"],
            description=trigger["description"],
            type=trigger["type"],
            amount=(trigger["change_amount"]) * -1,
            date_created=date_triggered,
            bucket_id=trigger["from_bucket_id"]
        )
        log_cruds.create_log(db=db, log=new_log)

    elif trigger["type"] == "MOV":

        # Subtracts from FROM BUCKET
        change_bucket_value(db_from_bucket, 'SUB',
                            trigger["change_amount"], db)

        # Then Adds to TO BUCKET
        change_bucket_value(db_to_bucket, 'ADD', trigger["change_amount"], db)

        new_log = log_schemas.LogCreate(
            name=trigger["name"],
            description=trigger["description"],
            type=trigger["type"],
            amount=(trigger["change_amount"]) * -1,
            date_created=date_triggered,
            bucket_id=trigger["from_bucket_id"]
        )
        log_cruds.create_log(db=db, log=new_log)

    elif trigger['type'] == "MULT":
        change_bucket_value(db_to_bucket, 'MULT',
                            trigger["change_amount"], db)

        new_log = log_schemas.LogCreate(
            name=trigger["name"],
            description=trigger["description"],
            type=trigger["type"],
            amount=((trigger["change_amount"]) + 1) * db_to_bucket,
            date_created=date_triggered,
            bucket_id=trigger["from_bucket_id"]
        )
        log_cruds.create_log(db=db, log=new_log)

    return {"Success": True}


def bring_forward(details: trigger_schemas.BringForwardBase, db: Session) -> Dict:

    db_flow_event = flow_event_cruds.get_flowEvent_by_id(
        db=db, id=details.flow_event_id)

    # Updates the time
    new_date = add_time(db_flow_event.next_trigger,
                        db_flow_event.frequency)

    flow_event_cruds.update_flowEvent_by_id(
        db=db,
        id=db_flow_event.id,
        new_flowEvent=flow_event_schemas.FlowEventUpdate(
            next_trigger=new_date)
    )

    # Moves money if needed
    if (details.money_include):
        trigger_details = {
            "name": db_flow_event.name,
            "description": db_flow_event.description,
            "change_amount": db_flow_event.change_amount,
            "type": db_flow_event.type,
            "from_bucket_id": db_flow_event.from_bucket_id,
            "to_bucket_id": db_flow_event.to_bucket_id
        }

        manual_trigger(trigger_details, db)

    return {"Success": True}
