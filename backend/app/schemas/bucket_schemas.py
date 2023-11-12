from typing import List, Union, Optional, Literal
from datetime import datetime
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
    from app.schemas.flow_event_schemas import FlowEventReadNR
    from_events: List[FlowEventReadNR]
    to_events: List[FlowEventReadNR]

# ======== UPDATE SCHEMAS ========

class BucketUpdate(BucketBase):
    name: Optional[str]
    description: Optional[str]
    current_amount: Optional[float]
    properties: Optional[BucketPropertiesBase]
