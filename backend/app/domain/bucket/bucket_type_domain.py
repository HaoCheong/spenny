
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field

class StoreBucket(BaseModel):
    type: Literal["STORE"]

class InvisibleBucket(BaseModel):
    type: Literal["INVSB"]

class GoalBucket(BaseModel):
    type: Literal["GOALS"]
    target: int

BucketType = Annotated[
    Union[
        GoalBucket,
        StoreBucket,
        InvisibleBucket,
        
    ],
    Field(discriminator="type")
]
