from typing import List, Optional, TYPE_CHECKING
from pydantic import BaseModel, ConfigDict
from datetime import datetime

if TYPE_CHECKING:
    pass

class AddBase(BaseModel):
    amount: int
    model_config = ConfigDict(extra="forbid")


class SubBase(BaseModel):
    amount: int
    model_config = ConfigDict(extra="forbid")


class MoveBase(BaseModel):
    to_bucket_id: int
    amount: int
    model_config = ConfigDict(extra="forbid")


class EventBase(BaseModel):
    ''' Events Base Schema '''
    
    name: str
    description: str
    trigger_datetime: datetime
    frequency: str
    event_type: str
    properties: AddBase | SubBase | MoveBase
    created_at: datetime
    updated_at: datetime

   # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)


class EventCreate(EventBase):
    ''' Event Create Schema '''
    pass


class EventReadNR(EventBase):
    ''' Event Read w/o relation Schema '''
    id: int


class EventReadWR(EventReadNR):
    ''' Event Read w/ relation Schema '''
    pass


class EventUpdate(EventBase):
    ''' Event update schema '''
    name: Optional[str] = None
    description: Optional[str] = None
    trigger_datetime: Optional[datetime] = None
    frequency: Optional[str] = None
    event_type: Optional[str] = None
    properties: Optional[AddBase | SubBase | MoveBase] = None

EventReadWR.model_rebuild()
