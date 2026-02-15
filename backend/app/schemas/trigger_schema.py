from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field

class TimedTrigger(BaseModel):
    type: Literal["timed"]
    frequency: str
    next_trigger_date: datetime

Trigger = Annotated[
    TimedTrigger,
    Field(discriminator="type")
]

