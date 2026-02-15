from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field
from datetime import datetime

from app.models.bucket_models import Bucket

class MoneyOperation(BaseModel):
    ''' Event that triggers related to money '''
    pass

class AddOperation(MoneyOperation):
    ''' Operation to Add Money to a bucket '''
    type: Literal["ADD"]
    amount: int

    def execute(self, bucket: Bucket):
        bucket.amount += self.amount

class SubOperation(MoneyOperation):
    ''' Operation to Subtract Money to a bucket '''
    type: Literal["SUB"]
    amount: int

    def execute(self, bucket: Bucket):
        bucket.amount -= self.amount

class MultOperation(MoneyOperation):
    ''' Operation to Multiply Money of a bucket '''
    type: Literal["MULT"]
    percentage: float

    def execute(self, bucket: Bucket):
        bucket.amount = bucket.amount * (1 + self.percentage)

# =============

class TranferMoneyOperation(MoneyOperation):
    ''' Operation related to transferring money from 1 bucket to another '''
    to_bucket_id: int

class MoveOperation(TranferMoneyOperation):
    ''' Operation to Move Money '''
    type: Literal["MOVE"]
    amount: int

    def execute(self, from_bucket: Bucket, to_bucket: Bucket):
        from_bucket.amount -= self.amount
        to_bucket.amount += self.amount

class CMVOperation(TranferMoneyOperation):
    ''' Operation to move money completely '''
    type: Literal["CMV"]

    def execute(self, from_bucket: Bucket, to_bucket: Bucket):
        to_transfer = from_bucket.amount
        from_bucket.amount = 0
        to_bucket.amount = to_transfer