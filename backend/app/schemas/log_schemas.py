from pydantic import BaseModel
from datetime import datetime


class LogBase(BaseModel):
    ''' Log Base Schema '''

    name: str
    description: str
    event_id: int
    event_type: str
    event_properties: dict
    bucket_id: int
    bucket_name: str


class LogCreate(LogBase):
    ''' Log Base Schema '''

    id: int
    created_at: datetime
    updated_at: datetime


class LogRead(LogBase):
    created_at: datetime
    updated_at: datetime

class LogTimeRange(BaseModel):
    start_date: datetime
    end_data: datetime



class LogAllRead(BaseModel):
    total: int
    data: list[LogRead]
