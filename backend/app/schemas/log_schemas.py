from typing import List, Union, Optional, Literal
from datetime import datetime
from pydantic import BaseModel

# ======== BASE SCHEMA ========

class LogBase(BaseModel):
    name: str
    description: str
    type: Literal["ADD", "SUB", "MOV"]
    amount: float
    date_created: datetime
    bucket_id: int

    class Config:
        orm_mode = True

# ======== CREATE SCHEMA ========

class LogCreate(LogBase):
    pass

# ======== READ SCHEMAS ========

class LogReadNR(LogBase):
    id: int

class LogReadWR(LogReadNR):
    from app.schemas.bucket_schemas import BucketReadNR
    bucket_id: int
    bucket: BucketReadNR

# ======== UPDATE SCHEMAS ========

class LogUpdate(LogBase):
    name: Optional[str]
    description: Optional[str]
    type: Optional[Literal["ADD", "SUB", "MOV"]]
    amount: Optional[float]
    date_created: Optional[str]