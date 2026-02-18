from abc import ABC, abstractmethod
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field
from datetime import datetime

from app.models.bucket_models import Bucket


class MoneyOperation(BaseModel):
    pass

class DirectMoneyOperation(MoneyOperation, ABC):
    ''' Event that triggers related to money '''
    
    @abstractmethod
    def apply(self, bucket):
        pass

class AddOperation(DirectMoneyOperation):
    ''' Operation to Add Money to a bucket '''
    type: Literal["ADD"]
    amount: int

    def execute(self, bucket: Bucket):
        bucket.amount += self.amount

class SubOperation(DirectMoneyOperation):
    ''' Operation to Subtract Money to a bucket '''
    type: Literal["SUB"]
    amount: int

    def execute(self, bucket: Bucket):
        bucket.amount -= self.amount

class MultOperation(DirectMoneyOperation):
    ''' Operation to Multiply Money of a bucket '''
    type: Literal["MULT"]
    percentage: float

    def execute(self, bucket: Bucket):
        bucket.amount = bucket.amount * (1 + self.percentage)

# =============

class TranferMoneyOperation(MoneyOperation, ABC):
    ''' Operation related to transferring money from 1 bucket to another '''
    to_bucket_id: int

    # STOPPED_HERE: Abstract method not working for transfermoneyoperation from bveing inheritted from operation

    @abstractmethod
    def apply(self, to_bucket: Bucket, from_bucket: Bucket):
        pass

class MoveOperation(TranferMoneyOperation):
    ''' Operation to Move Money '''
    type: Literal["MOVE"]
    amount: int

    def apply(self, to_bucket: Bucket, from_bucket: Bucket):
        from_bucket.amount -= self.amount
        to_bucket.amount += self.amount

class CMVOperation(TranferMoneyOperation):
    ''' Operation to move money completely '''
    type: Literal["CMV"]

    def apply(self, to_bucket: Bucket, from_bucket: Bucket):
        to_transfer = from_bucket.amount
        from_bucket.amount = 0
        to_bucket.amount = to_transfer