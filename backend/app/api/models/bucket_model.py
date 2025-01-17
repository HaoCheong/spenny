from app.database.database_manager import Base
from sqlalchemy import (JSON, Column, DateTime, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship


class Bucket(Base):
    __tablename__ = "buckets"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    current_amount = Column(Float)
    properties = Column(JSON) # Should be JSON when its

    logs = relationship("Log", back_populates="bucket")


    # from_events = relationship(
    #     "FlowEvent", back_populates="from_bucket", foreign_keys="FlowEvent.from_bucket_id")

    # to_events = relationship(
    #     "FlowEvent", back_populates="to_bucket", foreign_keys="FlowEvent.to_bucket_id")

    from_events = relationship(
        "FlowEvent", back_populates="from_bucket", foreign_keys="FlowEvent.from_bucket_id")

    to_events = relationship(
        "FlowEvent", back_populates="to_bucket", foreign_keys="FlowEvent.to_bucket_id")