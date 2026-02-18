from abc import ABC, abstractmethod
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field
from datetime import datetime
from app.operations.MoneyOperations.money_operations_schemas import MoneyOperation
from app.models.bucket_models import Bucket

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