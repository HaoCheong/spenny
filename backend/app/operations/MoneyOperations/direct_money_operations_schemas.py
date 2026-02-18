from abc import ABC, abstractmethod
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field
from datetime import datetime
from app.operations.MoneyOperations.money_operations_schemas import MoneyOperation
from app.models.bucket_models import Bucket

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