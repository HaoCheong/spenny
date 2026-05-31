from pydantic import BaseModel
from datetime import datetime
from typing import Literal, List


class LogBase(BaseModel):
    ''' Log Base Schema '''

    bucket_id: int
    bucket_name: str
    bucket_description: str

    event_id: int | None
    action_name: str
    action_description: str

    action_properties: dict

    created_at: datetime
    updated_at: datetime

class LogCreate(LogBase):
    ''' Log Base Schema '''
    pass


class LogRead(LogBase):
    id: int


class LogTimeRange(BaseModel):
    start_date: datetime
    end_date: datetime


class LogAllRead(BaseModel):
    total: int
    data: List[LogRead]
