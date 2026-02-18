from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field

from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field
from app.operations.MoneyOperations.direct_money_operations_schemas import AddOperation, SubOperation, MultOperation
from app.operations.MoneyOperations.transfer_money_operations_schemas import CMVOperation, MoveOperation

Operation = Annotated[
    Union[MoveOperation, AddOperation, SubOperation, MultOperation, CMVOperation],
    Field(discriminator="type")
]