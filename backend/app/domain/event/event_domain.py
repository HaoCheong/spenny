from app.domain.bucket.bucket_domain import BucketReadNR
from app.domain.event.operation_domain import Operation
from typing import List, Optional, TYPE_CHECKING, Union, Literal, Annotated
from pydantic import BaseModel, ConfigDict, Field, model_validator
from datetime import datetime
from app.domain.event.trigger_domain import Trigger

if TYPE_CHECKING:
    from app.domain.bucket.bucket_domain import BucketReadNR

class EventBase(BaseModel):
    ''' Events Base Schema '''

    name: str
    description: str
    bucket_id: int
    trigger: Trigger
    operation: Operation
    
    # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)

class EventCreate(EventBase):
    ''' Event Create Schema '''
    pass


class EventReadNR(EventBase):
    ''' Event Read w/o relation Schema '''
    id: int
    created_at: datetime
    updated_at: datetime


class EventReadWR(EventReadNR):
    ''' Event Read w/ relation Schema '''
    bucket: "BucketReadNR"


class EventAllRead(BaseModel):
    total: int
    data: list[EventReadNR]


class EventUpdate(EventBase):
    ''' Event update schema '''
    name: Optional[str] = None
    description: Optional[str] = None


EventReadWR.model_rebuild()
