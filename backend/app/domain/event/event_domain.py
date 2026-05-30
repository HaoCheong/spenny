from argparse import Action

from app.domain.bucket.bucket_domain import BucketReadNR
from app.domain.event.operation_domain import Operation
from typing import List, Optional, TYPE_CHECKING, Union, Literal, Annotated
from pydantic import BaseModel, ConfigDict, Field, model_validator
from datetime import datetime
from app.domain.event.trigger_domain import ManualTrigger, TimedTrigger, Trigger

if TYPE_CHECKING:
    from app.domain.bucket.bucket_domain import BucketReadNR

class ActionBase(BaseModel):
    name: str
    description: str
    bucket_id: int
    operation: Operation
    
    # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)

#PFIX: Not sure if this class here is the best thing
class ManualActionBase(ActionBase):
    trigger: ManualTrigger

class EventBase(ActionBase):
    trigger: TimedTrigger
    

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

# PFIX: Unsure how to deal with optional
class EventUpdate(EventBase):
    ''' Event update schema '''
    name: Optional[str] = None
    description: Optional[str] = None
    trigger: Optional[TimedTrigger] = None
    operation: Optional[Operation] = None

class EventTimeRange(BaseModel):
    start_datetime: Optional[datetime] = None
    end_datetime: datetime


EventReadWR.model_rebuild()
