from app.schemas.operation_schemas import MoneyOperation
from typing import Literal
from pydantic import BaseModel
from datetime import datetime

class AddEvent(MoneyOperation):
    ''' Event to Add Money to a bucket '''
    event_type: Literal["ADD"]
    amount: int

class SubEvent(MoneyOperation):
    ''' Event to Subtract Money to a bucket '''
    event_type: Literal["SUB"]
    amount: int

class MultEvent(MoneyOperation):
    ''' Event to Multiply Money of a bucket '''
    event_type: Literal["MULT"]
    percentage: float

class TranferMoneyEvent(MoneyOperation):
    ''' Event related to transferring money from 1 bucket to another '''
    to_bucket_id: int

class MoveEvent(TranferMoneyEvent):
    ''' Event to Move Money '''
    event_type: Literal["MOVE"]
    amount: int

class CMVEvent(TranferMoneyEvent):
    ''' Event to move money completely '''
    event_type: Literal["CMV"]