
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field

class StoreBucket(BaseModel):
    type: Literal["store"]

class InvisibleBucket(BaseModel):
    type: Literal["invisible"]

class GoalBucket(BaseModel):
    type: Literal["goal"]
    target: int

BucketType = Annotated[
    Union[
        StoreBucket,
        InvisibleBucket,
        GoalBucket
    ],
    Field(discriminator="type")
]
