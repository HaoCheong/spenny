from sqlalchemy import Column, ForeignKey, Float, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    amount = Column(Float)
    # date_created = Column(DateTime)
    date_created = Column(String)

    bucket_id = Column(Integer, ForeignKey("buckets.id"))
    bucket = relationship("Bucket", back_populates="logs")


class Bucket(Base):
    __tablename__ = "buckets"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    current_amount = Column(Float)

    logs = relationship("Log", back_populates="bucket")

    # from_events = relationship(
    #     "FlowEvent", back_populates="from_bucket")

    # to_events = relationship(
    #     "FlowEvent", back_populates="to_bucket")


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
    from_bucket = relationship("Bucket", foreign_keys=[
                               from_bucket_id])

    to_bucket_id = Column(Integer, ForeignKey("buckets.id"))
    # to_bucket_id = Column(Integer)
    to_bucket = relationship("Bucket", foreign_keys=[
                             to_bucket_id])
