from typing import List, Union, Optional, Literal
from datetime import datetime
from pydantic import BaseModel

# ======== BASE ========


class BucketBase(BaseModel):
    name: str
    description: str
    current_amount: float

    class Config:
        orm_mode = True


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


class LogBase(BaseModel):
    name: str
    description: str
    type: Literal["ADD", "SUB", "MOV"]
    amount: float
    date_created: datetime
    bucket_id: int

    class Config:
        orm_mode = True

# ======== CREATE ========


class BucketCreate(BucketBase):
    pass


class FlowEventCreate(FlowEventBase):
    next_trigger: datetime


class LogCreate(LogBase):
    pass

# ======== READNR ========


class BucketReadNR(BucketBase):
    id: int


class FlowEventReadNR(FlowEventBase):
    id: int
    next_trigger: datetime


class LogReadNR(LogBase):
    id: int
# ======== READWR ========


class BucketReadWR(BucketReadNR):
    from_events: List[FlowEventReadNR]
    to_events: List[FlowEventReadNR]


class FlowEventReadWR(FlowEventReadNR):
    from_bucket: Union[BucketReadNR, None]
    to_bucket: BucketReadNR


class LogReadWR(LogReadNR):
    bucket_id: int
    bucket: BucketReadNR

# ======== UPDATE ========


class BucketUpdate(BucketBase):
    name: Optional[str]
    description: Optional[str]
    current_amount: Optional[float]


class FlowEventUpdate(FlowEventBase):
    name: Optional[str]
    description: Optional[str]
    change_amount: Optional[float]
    type: Optional[Literal["ADD", "SUB", "MOV"]]
    frequency: Optional[str]
    next_trigger: Optional[datetime]
    from_bucket_id: Optional[int]
    to_bucket_id: Optional[int]


class LogUpdate(LogBase):
    name: Optional[str]
    description: Optional[str]
    type: Optional[Literal["ADD", "SUB", "MOV"]]
    amount: Optional[float]
    date_created: Optional[str]

# ======== TRIGGER ========


class TriggerBase(BaseModel):
    name: str
    description: str
    change_amount: float
    type: Literal["ADD", "SUB", "MOV"]
    from_bucket_id: Union[int, None]
    to_bucket_id: Union[int, None]
