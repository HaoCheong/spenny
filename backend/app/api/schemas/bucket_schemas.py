from datetime import datetime
from typing import List, Literal, Optional, Union

from pydantic import BaseModel

# ======== BASE SCHEMA ========

class BucketPropertiesBase(BaseModel):
    invisible: bool

class BucketBase(BaseModel):
    name: str
    description: str
    current_amount: float
    properties: BucketPropertiesBase

    class Config:
        orm_mode = True

# ======== CREATE SCHEMA ========

class BucketCreate(BucketBase):
    pass

# ======== READ SCHEMAS ========

class BucketReadNR(BucketBase):
    id: int

class BucketReadWR(BucketReadNR):
    from app.api.schemas.flow_event_schemas import FlowEventReadNR
    from_events: List[FlowEventReadNR]
    to_events: List[FlowEventReadNR]

# ======== UPDATE SCHEMAS ========

class BucketUpdate(BucketBase):
    name: Optional[str] = None
    description: Optional[str] = None
    current_amount: Optional[float] = None
    properties: Optional[BucketPropertiesBase] = None
