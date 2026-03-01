from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field

from datetime import datetime
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field
from app.domain.event.money.direct_money_operations_domain import AddOperation, SubOperation, MultOperation
from app.domain.event.money.transfer_money_operations_domain import CMVOperation, MoveOperation

Operation = Annotated[
    Union[MoveOperation, AddOperation, SubOperation, MultOperation, CMVOperation],
    Field(discriminator="type")
]