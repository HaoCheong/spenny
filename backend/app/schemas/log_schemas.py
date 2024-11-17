from datetime import datetime
from typing import List, Literal, Optional, Union

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
    bucket: Union[BucketReadNR, None]

# ======== UPDATE SCHEMAS ========

class LogUpdate(LogBase):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Literal["ADD", "SUB", "MOV"]] = None
    amount: Optional[float] = None
    date_created: Optional[datetime] = None