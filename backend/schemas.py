from typing import List, Union, Optional
from pydantic import BaseModel

# ======== BASE ========


class BucketBase(BaseModel):
    name: str
    description: str
    current_amount: int


class FlowEventBase(BaseModel):
    name: str
    description: str
    type: str
    from_id: Union[int, None]
    to_id: Union[int, None]

# ======== CREATE ========


class BucketCreate(BucketBase):
    id: int


class FlowEventCreate(FlowEventBase):
    id: int
# ======== READNR ========


class BucketReadNR(BucketBase):
    id: int


class FlowEventReadNR(FlowEventBase):
    id: int

# ======== READWR ========


class BucketReadWR(BucketReadNR):
    pass


class FlowEventReadWR(FlowEventReadNR):
    pass

# ======== UPDATE ========


class BucketUpdate(BucketBase):
    name: Optional[str]
    description: Optional[str]
    current_amount: Optional[int]


class FlowEventUpdate(FlowEventBase):
    name: Optional[str]
    description: Optional[str]
    type: Optional[str]
