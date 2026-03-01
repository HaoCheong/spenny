from typing import List, Optional, TYPE_CHECKING, Literal
from pydantic import BaseModel, ConfigDict, model_validator
from datetime import datetime

from backend.app.operations.BucketOperations.bucketType_schemas import BucketType

if TYPE_CHECKING:
    from app.operations.event_schemas import EventReadNR

class BucketBase(BaseModel):
    ''' Buckets Base Schema '''

    name: str
    description: str
    amount: int
    variant: BucketType

    # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)


class BucketCreate(BucketBase):
    ''' Bucket Create Schema '''
    pass


class BucketReadNR(BucketBase):
    ''' Bucket Read w/o relation Schema '''
    id: int
    properties: Optional[dict] = None
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
    bucket_type: Optional[str] = None
    properties: Optional[dict] = None


class BucketAllRead(BaseModel):
    total: int
    data: list[BucketReadNR]

from app.operations.event_schemas import EventReadNR
BucketReadWR.model_rebuild()
