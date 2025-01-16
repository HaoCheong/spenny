from app.database.database_manager import Base
from sqlalchemy import (JSON, Column, DateTime, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship


class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    amount = Column(Float)
    date_created = Column(DateTime)

    # Bucket Relationship
    bucket_id = Column(Integer, ForeignKey("buckets.id"))
    bucket = relationship("Bucket", back_populates="logs")