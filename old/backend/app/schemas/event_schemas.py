from app.schemas.bucket_schemas import BucketReadNR
from typing import List, Optional, TYPE_CHECKING, Union, Literal, Annotated
from pydantic import BaseModel, ConfigDict, Field, model_validator
from datetime import datetime

if TYPE_CHECKING:
    from app.schemas.bucket_schemas import BucketReadNR


class AddProps(BaseModel):
    ''' Properties required for ADD (Adding amount into a bucket) '''
    amount: int


class SubProps(BaseModel):
    ''' Properties required for SUB (Subtracting amount into a bucket) '''
    amount: int


class MoveProps(BaseModel):
    ''' Properties required for MOVE (Moving a set amount from the current bucket into another bucket) '''
    to_bucket_id: int
    amount: int


class MultProps(BaseModel):
    ''' Properties required for MULT (Increase the current bucket amount by a percentage) '''
    percentage: float


class CMVProps(BaseModel):
    ''' Properties required for CMV (Clear and MoVe, Taking all that is remaining in the current bucket and moving it to another bucket) '''
    to_bucket_id: int


class EventBase(BaseModel):
    ''' Events Base Schema '''

    name: str
    description: str
    trigger_datetime: datetime
    frequency: str
    event_type: Literal["ADD", "SUB", "MOVE", "MULT", "CMV"] | None
    properties: dict

    # PFIX: Might require moving to discrimnated union
    @model_validator(mode='after')
    def validate_properties(self):
        if self.event_type == "ADD":
            self.properties = AddProps(**self.properties)
        elif self.event_type == "SUB":
            self.properties = SubProps(**self.properties)
        elif self.event_type == "MOVE":
            self.properties = MoveProps(**self.properties)
        elif self.event_type == "MULT":
            self.properties = MultProps(**self.properties)
        elif self.event_type == "CMV":
            self.properties = CMVProps(**self.properties)
        elif self.event_type is None:
            self.properties == None
        else:
            raise ValueError(
                f"Unknown properties for event type {self.event_type}")

        return self

   # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)


class EventCreate(EventBase):
    ''' Event Create Schema '''
    bucket_id: int


class EventReadNR(EventBase):
    ''' Event Read w/o relation Schema '''
    id: int
    bucket_id: int
    created_at: datetime
    updated_at: datetime


class EventReadWR(EventReadNR):
    ''' Event Read w/ relation Schema '''
    bucket: "BucketReadNR"


class EventUpdate(EventBase):
    ''' Event update schema '''
    name: Optional[str] = None
    description: Optional[str] = None
    trigger_datetime: Optional[datetime] = None
    frequency: Optional[str] = None
    event_type: Optional[str] = None
    properties: Optional[dict] = None


class EventPushOptions(BaseModel):
    # True means money will be affected, False means money will not be affected
    change_amount: bool


class EventTimeframe(BaseModel):
    first_date: datetime | None
    last_date: datetime


class EventAllRead(BaseModel):
    total: int
    data: list[EventReadNR]


EventReadWR.model_rebuild()
