from sqlalchemy import Column, ForeignKey, Float, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Bucket(Base):
    __tablename__ = "buckets"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    current_amount = Column(Float)

    from_events = relationship(
        "FlowEvent")
    # to_events = relationship(
    #     "FlowEvent", foreign_keys='to_bucket_id')


class FlowEvent(Base):
    __tablename__ = "flowEvents"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    change_amount = Column(Float)
    type = Column(String)
    frequency = Column(String)
    # next_trigger = Column(DateTime)
    from_bucket_id = Column(Integer, ForeignKey("buckets.id"))
    # from_bucket_id = Column(Integer)
    from_bucket = relationship("Bucket", back_populates="from_events")

    # to_bucket_id = Column(Integer, ForeignKey("buckets.id"))
    # # to_bucket_id = Column(Integer)
    # to_bucket = relationship("Bucket", back_populates="to_events")
