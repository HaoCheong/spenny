from sqlalchemy import Column, ForeignKey, Float, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Bucket(Base):
    __tablename__ = "buckets"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    current_amount = Column(Float)


class FlowEvent(Base):
    __tablename__ = "flowEvents"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    from_id = Column(Integer, ForeignKey("buckets.id"))
    to_id = Column(Integer, ForeignKey("buckets.id"))
