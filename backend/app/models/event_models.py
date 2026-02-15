from sqlalchemy import Integer, String, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.database.database import Base
from datetime import datetime

class Event(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    trigger: Mapped[dict] = mapped_column(JSON)
    operation: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    bucket_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("buckets.id"), nullable=True)
    bucket: Mapped["Bucket"] = relationship(
        "Bucket", back_populates="events", uselist=False)

    class Config:
        orm_mode = True
