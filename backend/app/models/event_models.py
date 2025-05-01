from sqlalchemy import Integer, String, Boolean, DateTime, JSON
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.database.database import Base
from datetime import datetime


class Event(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    trigger_datetime: Mapped[datetime] = mapped_column(DateTime)
    frequency: Mapped[str] = mapped_column(String)
    event_type: Mapped[str] = mapped_column(String)
    properties: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
