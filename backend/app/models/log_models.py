from sqlalchemy import Integer, String, Boolean, DateTime, JSON
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.database.database import Base
from datetime import datetime

from app.utils.DatetimeJSON import DatetimeJSON


class Log(Base):

    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    bucket_id: Mapped[int] = mapped_column(Integer)
    bucket_name: Mapped[str] = mapped_column(String)
    bucket_description: Mapped[str] = mapped_column(String)

    event_id: Mapped[int] = mapped_column(Integer)
    event_name: Mapped[str] = mapped_column(String)
    event_description: Mapped[str] = mapped_column(String)
    
    event_properties: Mapped[dict] = mapped_column(DatetimeJSON)

    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    
    class Config:
        orm_mode = True
