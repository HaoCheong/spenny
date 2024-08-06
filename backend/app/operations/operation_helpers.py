from typing import Dict, List
from app.schemas.bucket_schemas import BucketReadWR, BucketUpdate, BucketReadNR
from app.schemas.log_schemas import LogCreate, LogReadNR
from app.cruds.bucket_cruds import update_bucket_by_id
from app.cruds.log_cruds import create_log
from sqlalchemy.orm import Session
from datetime import datetime


def change_bucket_value(bucket: BucketReadWR, op: str, change_amount: float, db: Session) -> BucketReadNR:
    '''
    Given a bucket and an operation, update the bucket value by a given amount
    '''
    new_bucket = None

    if (op == "SUB"):
        new_value = round(
            bucket["current_amount"] - change_amount, 2)

    elif (op == "ADD"):
        new_value = round(
            bucket["current_amount"] + change_amount, 2)

    new_bucket = BucketUpdate(current_amount=new_value)

    update_bucket_by_id(
        db=db, id=bucket["id"], new_bucket=new_bucket)

    return new_bucket


def log_operation(log_details: Dict, log_time: datetime, db: Session) -> LogReadNR:
    '''
    Wraps the creation and the logging
    '''

    # PFIX: IDK if this really simplifies anything
    new_log = LogCreate(
        name=log_details["name"],
        description=log_details["description"],
        type=log_details['type'],
        amount=(log_details["change_amount"]) * -1,
        date_created=log_time,
        bucket_id=log_details["from_bucket_id"]
    )
    create_log(db=db, log=new_log)

    return new_log
