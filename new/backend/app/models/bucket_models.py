from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.event_models import Event, EventReadNR

class BucketBase(SQLModel):
    
    name: str = Field(index=True)
    description: str = Field(index=True, unique=True)
    amount: int = Field(default=0)
    is_invisible: bool = Field(default=False)
    
    created_at: datetime = Field(default=None)
    updated_at: datetime = Field(default=None)

class Bucket(BucketBase, table=True):

    __tablename__ = 'buckets'

    id: int = Field(default=None, primary_key=True)
    
    events: list["Event"] = Relationship(back_populates='bucket')

class BucketReadNR(BucketBase):
    id: int

class BucketReadWR(BucketReadNR):
    
    events: list["EventReadNR"] = []

class BucketCreate(BucketBase):
    pass

class BucketUpdate(BucketBase):
    name: str | None = None
    description: str | None = None
    amount: int | None = None
    is_invisible: bool | None = None

from app.models.event_models import EventReadNR

BucketReadWR.model_rebuild()
