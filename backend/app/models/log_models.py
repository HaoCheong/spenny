from sqlalchemy import Integer, String, Boolean, DateTime, JSON
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.database.database import Base
from datetime import datetime


class Log(Base):

    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)

    event_id: Mapped[int] = mapped_column(Integer)
    event_type: Mapped[str] = mapped_column(String)
    event_properties: Mapped[dict] = mapped_column(JSON)

    bucket_id: Mapped[int] = mapped_column(Integer)
    bucket_name: Mapped[str] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)