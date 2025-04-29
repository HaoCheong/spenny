from typing import List, Optional, TYPE_CHECKING
from pydantic import BaseModel, ConfigDict
from datetime import datetime

if TYPE_CHECKING:
    pass


class BucketBase(BaseModel):
    ''' Buckets Base Schema '''
    
    name: str
    description: str
    amount: int
    is_invisible: bool
    created_at: datetime
    updated_at: datetime

   # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)


class BucketCreate(BucketBase):
    ''' Bucket Create Schema '''
    pass


class BucketReadNR(BucketBase):
    ''' Bucket Read w/o relation Schema '''
    id: int


class BucketReadWR(BucketReadNR):
    ''' Bucket Read w/ relation Schema '''
    pass


class BucketUpdate(BucketBase):
    ''' Bucket update schema '''
    name: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[int] = None
    is_invisible: Optional[bool] = None

BucketReadWR.model_rebuild()
