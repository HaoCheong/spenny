from typing import List, Union, Optional, Literal
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

# ======== CREATE ========


class BucketCreate(BucketBase):
    pass


class FlowEventCreate(FlowEventBase):
    pass
# ======== READNR ========


class BucketReadNR(BucketBase):
    id: int


class FlowEventReadNR(FlowEventBase):
    id: int

# ======== READWR ========


class BucketReadWR(BucketReadNR):
    from_events: List[FlowEventReadNR]
    # to_events: List[FlowEventReadNR]


class FlowEventReadWR(FlowEventReadNR):
    from_bucket: BucketReadNR
    # to_bucket: BucketReadNR

# ======== UPDATE ========


class BucketUpdate(BucketBase):
    name: Optional[str]
    description: Optional[str]
    current_amount: Optional[float]


class FlowEventUpdate(FlowEventBase):
    name: Optional[str]
    description: Optional[str]
    type: Optional[str]
