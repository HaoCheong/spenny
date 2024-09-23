from typing import Dict, List
from app.api.schemas.bucket_schemas import BucketReadWR, BucketUpdate, BucketReadNR
from app.api.schemas.log_schemas import LogCreate, LogReadNR
from app.api.cruds.bucket_cruds import update_bucket_by_id
from app.api.cruds.log_cruds import create_log
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

    elif (op == "MULT"):
        new_value = round(
            bucket["current_amount"] * (1 + change_amount), 2)

    new_bucket = BucketUpdate(current_amount=new_value)

    update_bucket_by_id(
        db=db, id=bucket["id"], new_bucket=new_bucket)

    return new_bucket
