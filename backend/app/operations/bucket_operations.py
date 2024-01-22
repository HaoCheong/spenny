from sqlalchemy.orm import Session
from datetime import datetime
from app.helpers import add_time

from fastapi.encoders import jsonable_encoder

# Update a singular bucket value
import app.cruds.bucket_cruds as bucket_cruds
import app.cruds.log_cruds as log_cruds
import app.cruds.flow_event_cruds as flow_event_cruds

import app.schemas.flow_event_schemas as flow_event_schemas
import app.schemas.bucket_schemas as bucket_schemas
import app.schemas.log_schemas as log_schemas


def update_bucket_values(fe: flow_event_schemas.FlowEventReadNR, db: Session, old_date: datetime):
    '''
    Updates the bucket valuies based on the Flow Event
    '''    
    # Grab the two potential buckets
    from_bucket = None
    to_bucket = None

    if (fe.from_bucket_id is not None):
        from_bucket = jsonable_encoder(
            bucket_cruds.get_bucket_by_id(
                db=db,
                id=fe.from_bucket_id
            )
        )

        # update bucket value
        if (fe.type == "SUB" or fe.type == "MOV"):
            new_value = from_bucket["current_amount"] - fe.change_amount
            new_bucket = bucket_schemas.BucketUpdate(current_amount=new_value)
            bucket_cruds.update_bucket_by_id(
                db=db,
                id=fe.from_bucket_id,
                new_bucket=new_bucket
            )
            
            # create log
            new_log = log_schemas.LogCreate(
                name=fe.name,
                description=fe.description,
                type=fe.type,
                amount=(fe.change_amount) * -1,
                date_created=old_date,
                bucket_id=fe.from_bucket_id
            )
            log_cruds.create_log(db=db, log=new_log)

    if (fe.to_bucket_id is not None):

        to_bucket = jsonable_encoder(bucket_cruds.get_bucket_by_id(db=db, id=fe.to_bucket_id))

        # update bucket value
        if (fe.type == "ADD" or fe.type == "MOV"):
            new_value = to_bucket["current_amount"] + fe.change_amount
            new_bucket = bucket_schemas.BucketUpdate(current_amount=new_value)
            bucket_cruds.update_bucket_by_id(
                db=db,
                id=fe.to_bucket_id,
                new_bucket=new_bucket
            )
            
            # create log
            new_log = log_schemas.LogCreate(
                name=fe.name,
                description=fe.description,
                type=fe.type,
                amount=fe.change_amount,
                date_created=old_date,
                bucket_id=fe.to_bucket_id
            )
            log_cruds.create_log(
                db=db,
                log=new_log
            )

# Iterate through all flow events and update their value
def update_all_buckets(db: Session):
    ''' Update all the buckets based on the flow event '''
 
    # Get all Flow Events
    flowEvents = flow_event_cruds.get_all_flowEvents(db=db)

    for fe in flowEvents:

        # Checks if its time to trigger yet
        date_now = datetime.now()
        if (date_now < fe.next_trigger):
            continue

        # Will loop until current fe next trigger is past the current time (Useful if long time no trigger)
        curr_fe = fe
        while (date_now > curr_fe.next_trigger):

            # Update the next trigger date
            new_date = add_time(curr_fe.next_trigger, curr_fe.frequency)
            
            res = flow_event_cruds.update_flowEvent_by_id(
                db=db,
                id=curr_fe.id,
                new_flowEvent=flow_event_schemas.FlowEventUpdate(next_trigger=new_date)
            )

            # Update the related buckets value
            update_bucket_values(
                fe=res,
                db=db,
                old_date=curr_fe.next_trigger
            )

            # Set values for next loop
            curr_fe = res
            date_now = datetime.now()

    return {"Success": True}