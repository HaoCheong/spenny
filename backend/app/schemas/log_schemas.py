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
    created_at: datetime
    updated_at: datetime

class LogCreate(LogBase):
    ''' Log Base Schema '''
    
    id: int

class LogRead(LogBase):
    pass


class LogAllRead(BaseModel):
    total: int
    data: list[LogRead]

