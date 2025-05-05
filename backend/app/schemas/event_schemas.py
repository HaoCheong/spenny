from typing import List, Optional, TYPE_CHECKING, Union, Literal, Annotated
from pydantic import BaseModel, ConfigDict, Field, model_validator
from datetime import datetime

if TYPE_CHECKING:
    pass

class AddProps(BaseModel):
    amount: int

class SubProps(BaseModel):
    amount: int

class MoveProps(BaseModel):
    to_bucket_id: int
    amount: int

class EventBase(BaseModel):
    ''' Events Base Schema '''
    
    name: str
    description: str
    trigger_datetime: datetime
    frequency: str
    event_type: Literal["ADD", "SUB", "MOVE"]
    properties: dict
    created_at: datetime
    updated_at: datetime

    # PFIX: Might require moving to discrimnated union
    @model_validator(mode='after')
    def validate_properties(self):
        if self.event_type == "ADD":
            self.properties = AddProps(**self.properties)
        elif self.event_type == "SUB":
            self.properties = SubProps(**self.properties)
        elif self.event_type == "MOVE":
            self.properties = MoveProps(**self.properties)
        else:
            raise ValueError(f"Unknown properties for event type {self.event_type}")

        return self
    
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
    properties: Optional[dict] = None

EventReadWR.model_rebuild()
