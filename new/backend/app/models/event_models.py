from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import JSON, Field, Relationship, SQLModel, Column

if TYPE_CHECKING:
    from app.models.bucket_models import Bucket, BucketReadNR

class AddBase(SQLModel):
    amount: int

class SubBase(SQLModel):
    amount: int

class MoveBase(SQLModel):
    to_bucket_id: int
    amount: int

class EventBase(SQLModel):
    
    name: str = Field(index=True)
    description: str = Field(index=True)
    trigger_datetime: datetime = Field(default=None)
    frequency: str = Field(default=None)
    event_type: str = Field(default=None)
    properties: dict = Field(default_factory=dict, sa_column=Column(JSON))
    created_at: datetime = Field(default=None)
    updated_at: datetime = Field(default=None)

    class Config:
        arbitrary_types_allowed = True

class Event(EventBase, table=True):

    __tablename__ = 'events'

    id: int = Field(default=None, primary_key=True)
    bucket_id: Optional[int] = Field(default=None, foreign_key="buckets.id")
    bucket: Optional["Bucket"] = Relationship(back_populates="events")

class EventReadNR(EventBase):
    id: int

class EventReadWR(EventReadNR):
    bucket: Optional["BucketReadNR"] = None

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    name: str | None = None
    description: str | None = None
    trigger_datetime: datetime | None = None
    frequency: str | None = None
    event_type: str | None = None
    properties: dict | None = None

from app.models.bucket_models import BucketReadNR

EventReadWR.model_rebuild()
