from typing import List, Union, Optional, Literal
from datetime import datetime
from pydantic import BaseModel

# ======== BASE SCHEMA ========

class FlowEventBase(BaseModel):
    name: str
    description: str
    change_amount: float
    type: Literal["ADD", "SUB", "MOV"]
    frequency: str
    from_bucket_id: Union[int, None]
    to_bucket_id: Union[int, None]

    class Config:
        orm_mode = True

# ======== CREATE SCHEMA ========

class FlowEventCreate(FlowEventBase):
    next_trigger: datetime

# ======== READ SCHEMAS ========

class FlowEventReadNR(FlowEventBase):
    id: int
    next_trigger: datetime

class FlowEventReadWR(FlowEventReadNR):
    from app.schemas.bucket_schemas import BucketReadNR
    from_bucket: Union[BucketReadNR, None]
    to_bucket: BucketReadNR

# ======== UPDATE SCHEMAS ========

class FlowEventUpdate(FlowEventBase):
    name: Optional[str]
    description: Optional[str]
    change_amount: Optional[float]
    type: Optional[Literal["ADD", "SUB", "MOV"]]
    frequency: Optional[str]
    next_trigger: Optional[datetime]
    from_bucket_id: Optional[int]
    to_bucket_id: Optional[int]