from typing import List, Optional, TYPE_CHECKING
from pydantic import BaseModel, ConfigDict
from datetime import datetime

if TYPE_CHECKING:
    from app.schemas.event_schemas import EventReadNR


class BucketBase(BaseModel):
    ''' Buckets Base Schema '''

    name: str
    description: str
    amount: int
    is_invisible: bool

   # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)


class BucketCreate(BucketBase):
    ''' Bucket Create Schema '''
    created_at: datetime
    updated_at: datetime


class BucketReadNR(BucketBase):
    ''' Bucket Read w/o relation Schema '''
    id: int
    created_at: datetime
    updated_at: datetime


class BucketReadWR(BucketReadNR):
    ''' Bucket Read w/ relation Schema '''
    events: List["EventReadNR"]


class BucketUpdate(BucketBase):
    ''' Bucket update schema '''
    name: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[int] = None
    is_invisible: Optional[bool] = None
    updated_at: datetime


class BucketAllRead(BaseModel):
    total: int
    data: list[BucketReadNR]

from app.schemas.event_schemas import EventReadNR
BucketReadWR.model_rebuild()
