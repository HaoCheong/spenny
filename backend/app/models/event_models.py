from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from sqlalchemy.orm import relationship
from app.database.database import Base


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    trigger_datetime = Column(DateTime)
    frequency = Column(String)
    event_type = Column(String)
    properties = Column(JSON)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)