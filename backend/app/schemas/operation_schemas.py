from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field

from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field
from app.schemas.money_operations_schemas import AddOperation, SubOperation, MultOperation, MoveOperation, CMVOperation

Operation = Annotated[
    Union[MoveOperation, AddOperation, SubOperation, MultOperation, CMVOperation],
    Field(discriminator="type")
]