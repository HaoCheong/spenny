from sqlalchemy import Column, ForeignKey, Float, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from database import Base



class Bucket(Base):
    __tablename__ = "buckets"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    current_amount = Column(Float)
    properties = Column(JSON) # Should be JSON when its

    logs = relationship("Log", back_populates="bucket")

    from_events = relationship(
        "FlowEvent", back_populates="from_bucket")

    to_events = relationship(
        "FlowEvent", back_populates="to_bucket")