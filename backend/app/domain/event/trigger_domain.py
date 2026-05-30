from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field

class TimedTrigger(BaseModel):
    type: Literal["timed"]
    frequency: str
    next_trigger_date: datetime

# PFIX: Might be redundant but it is extensible so alas Imma leave it
class ManualTrigger(BaseModel):
    type: Literal["manual"]

Trigger = Annotated[
    TimedTrigger,
    ManualTrigger,
    Field(discriminator="type")
]

