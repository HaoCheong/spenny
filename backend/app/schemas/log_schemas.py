from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class LogBase(BaseModel):
    ''' Log Base Schema '''

    name: str
    description: str
    log_type: Literal['EDIT', 'EVENT']
    event_id: int
    event_type: str
    event_properties: dict
    bucket_id: int
    bucket_name: str


class LogCreate(LogBase):
    ''' Log Base Schema '''

    created_at: datetime
    updated_at: datetime


class LogRead(LogBase):
    id: int
    created_at: datetime
    updated_at: datetime


class LogTimeRange(BaseModel):
    start_date: datetime
    end_date: datetime


class LogAllRead(BaseModel):
    total: int
    data: list[LogRead]
