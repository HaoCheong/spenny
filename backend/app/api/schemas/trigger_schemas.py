from typing import List, Union, Optional, Literal
from datetime import datetime
from pydantic import BaseModel

# ======== BASE SCHEMA ========

class TriggerBase(BaseModel):
    name: str
    description: str
    change_amount: float
    type: Literal["ADD", "SUB", "MOV"]
    from_bucket_id: Union[int, None]
    to_bucket_id: Union[int, None]

class BringForwardBase(BaseModel):
    money_include: bool
    flow_event_id: int

