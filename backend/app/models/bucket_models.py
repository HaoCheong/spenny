from sqlalchemy import Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.inspection import inspect
from app.database.database import Base
from datetime import datetime


class Bucket(Base):

    __tablename__ = "buckets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    amount: Mapped[float] = mapped_column(Integer)
    bucket_type: Mapped[str] = mapped_column(String)
    properties: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    events: Mapped[list['Event']] = relationship(
        "Event", back_populates="bucket")

    class Config:
        orm_mode = True
