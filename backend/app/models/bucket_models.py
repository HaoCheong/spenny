from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.database.database import Base


class Bucket(Base):

    __tablename__ = "buckets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    amount = Column(Integer)
    is_invisible = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)