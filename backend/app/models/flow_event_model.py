from sqlalchemy import Column, ForeignKey, Float, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from database import Base

class FlowEvent(Base):
    __tablename__ = "flowEvents"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    change_amount = Column(Float)
    type = Column(String)
    frequency = Column(String)
    next_trigger = Column(DateTime)

    from_bucket_id = Column(Integer, ForeignKey("buckets.id"))
    from_bucket = relationship("Bucket", foreign_keys=[
                               from_bucket_id])

    to_bucket_id = Column(Integer, ForeignKey("buckets.id"))
    to_bucket = relationship("Bucket", foreign_keys=[
                             to_bucket_id])
