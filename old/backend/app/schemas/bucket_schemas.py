from typing import List, Optional, TYPE_CHECKING, Literal
from pydantic import BaseModel, ConfigDict, model_validator
from datetime import datetime

if TYPE_CHECKING:
    from app.schemas.event_schemas import EventReadNR

class StoreProps(BaseModel):
    pass

class InvisibleProps(BaseModel):
    pass

class GoalProps(BaseModel):
    target: int

class BucketBase(BaseModel):
    ''' Buckets Base Schema '''

    name: str
    description: str
    amount: int
    bucket_type: Literal["STORE", "INVSB", "GOALS"] | None
    properties: dict | None 

    @model_validator(mode='after')
    def validate_properties(self):
        if self.bucket_type == "STORE":
            self.properties = None
        elif self.bucket_type == "INVSB":
            self.properties = None
        elif self.bucket_type == "GOALS":
            self.properties = GoalProps(**self.properties)
        elif self.bucket_type is None:
            self.properties == None
        else:
            raise ValueError(
                f"Unknown properties for bucket type {self.bucket_type}")

        return self

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

from app.schemas.event_schemas import EventReadNR
BucketReadWR.model_rebuild()
