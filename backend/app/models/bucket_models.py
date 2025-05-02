from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.database.database import Base
from datetime import datetime


class Bucket(Base):

    __tablename__ = "buckets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    amount: Mapped[int] = mapped_column(Integer)
    is_invisible: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    events: Mapped[list['Event']] = relationship("Event", back_populates="bucket")