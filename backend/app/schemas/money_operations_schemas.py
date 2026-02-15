from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field
from datetime import datetime

class MoneyOperation(BaseModel):
    ''' Event that triggers related to money '''
    pass

class AddOperation(MoneyOperation):
    ''' Operation to Add Money to a bucket '''
    type: Literal["ADD"]
    amount: int

class SubOperation(MoneyOperation):
    ''' Operation to Subtract Money to a bucket '''
    type: Literal["SUB"]
    amount: int

class MultOperation(MoneyOperation):
    ''' Operation to Multiply Money of a bucket '''
    type: Literal["MULT"]
    percentage: float

# =============

class TranferMoneyOperation(MoneyOperation):
    ''' Operation related to transferring money from 1 bucket to another '''
    to_bucket_id: int

class MoveOperation(TranferMoneyOperation):
    ''' Operation to Move Money '''
    type: Literal["MOVE"]
    amount: int

class CMVOperation(TranferMoneyOperation):
    ''' Operation to move money completely '''
    type: Literal["CMV"]