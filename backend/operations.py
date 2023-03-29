from sqlalchemy.orm import Session
import models
import schemas
import cruds
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from helpers import add_time

# Update a singular bucket value


def update_bucket_values(fe: schemas.FlowEventReadNR, db: Session, old_date: datetime):
    # Grab the two potential buckets
    from_bucket = None
    to_bucket = None

    if (fe.from_bucket_id is not None):
        from_bucket = cruds.get_bucket_by_id(db=db, id=fe.from_bucket_id)
        # update bucket value
        if (fe.type == "SUB" or fe.type == "MOV"):
            new_value = from_bucket["current_amount"] - fe.change_amount
            new_bucket = schemas.BucketUpdate(current_amount=new_value)
            cruds.update_bucket_by_id(
                db=db, id=fe.from_bucket_id, new_bucket=new_bucket)
            # create log
            new_log = schemas.LogCreate(
                name=fe.name,
                description=fe.description,
                type=fe.type,
                amount=(fe.change_amount) * -1,
                date_created=old_date,
                bucket_id=fe.from_bucket_id
            )
            cruds.create_log(db=db, log=new_log)

    if (fe.to_bucket_id is not None):
        to_bucket = cruds.get_bucket_by_id(db=db, id=fe.to_bucket_id)
        # update bucket value
        if (fe.type == "ADD" or fe.type == "MOV"):
            new_value = to_bucket["current_amount"] + fe.change_amount
            new_bucket = schemas.BucketUpdate(current_amount=new_value)
            cruds.update_bucket_by_id(
                db=db, id=fe.to_bucket_id, new_bucket=new_bucket)
            # create log
            new_log = schemas.LogCreate(
                name=fe.name,
                description=fe.description,
                type=fe.type,
                amount=fe.change_amount,
                date_created=old_date,
                bucket_id=fe.to_bucket_id
            )
            cruds.create_log(db=db, log=new_log)


# Iterate through all flow events and update their value
def update_all_buckets(db: Session):

    # Get all flow
    flowEvents = cruds.get_all_flowEvents(db=db)

    # For each flow
    for fe in flowEvents:

        # Checks if its time to trigger yet
        date_now = datetime.now()
        if (date_now < fe.next_trigger):
            continue

        # Will loop until current fe next trigger is past the current time (Useful if long time no trigger)
        curr_fe = fe
        while (date_now > curr_fe.next_trigger):

            # Update the dates
            new_date = add_time(curr_fe.next_trigger, curr_fe.frequency)
            changed_fe = {"next_trigger": new_date}
            res = cruds.update_flowEvent_by_id(
                db=db, id=curr_fe.id, new_flowEvent=schemas.FlowEventUpdate(next_trigger=new_date))

            # Update individual buckets
            update_bucket_values(fe=res, db=db, old_date=curr_fe.next_trigger)

            # Set values for next loop
            curr_fe = res
            date_now = datetime.now()

    return {"Success": True}
