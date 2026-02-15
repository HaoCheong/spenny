from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field

class MoneyOperation(BaseModel):
    ''' Event that triggers related to money '''
    type: Literal["money"]

Operation = Annotated[
    MoneyOperation,
    Field(discriminator="type")
]