from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database_manager import Base


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
    from_bucket = relationship("Bucket", back_populates="from_events", foreign_keys=[from_bucket_id])

    to_bucket_id = Column(Integer, ForeignKey("buckets.id"))
    to_bucket = relationship("Bucket", back_populates="to_events", foreign_keys=[to_bucket_id])
