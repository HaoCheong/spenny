from sqlalchemy.orm import Session
import models
import schemas
import cruds
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from helpers import add_time

# Update a singular bucket value


def update_bucket_values(fe: schemas.FlowEventReadNR, db: Session):
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
                date_created=datetime.now(),
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
                date_created=datetime.now(),
                bucket_id=fe.to_bucket_id
            )
            cruds.create_log(db=db, log=new_log)
    # print("FROM BUCKET", from_bucket)
    # print("TO BUCKET", to_bucket)


# Iterate through all flow events and update their value
def update_all_buckets(db: Session):

    # Get all flow
    flowEvents = cruds.get_all_flowEvents(db=db)

    # For each flow
    for fe in flowEvents:

        # Checks if its time to trigger yet
        date_now = datetime.now()
        if (date_now < fe.next_trigger):
            print("NOT YET", date_now, fe.next_trigger)
            continue

        # Alter next trigger in flowEvent
        new_date = add_time(fe.next_trigger, fe.frequency)

        # Updating FlowEvent Dates
        changed_fe = {"next_trigger": new_date}
        res = cruds.update_flowEvent_by_id(
            db=db, id=fe.id, new_flowEvent=schemas.FlowEventUpdate(next_trigger=new_date))

        # Updating Bucket Values
        update_bucket_values(fe=res, db=db)

    return {"Success": True}
