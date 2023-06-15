import cruds
import json
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from database import SessionLocal, engine
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_time(date, sum_date):
    # Grab the last character
    increment_size = sum_date[-1]
    amount = int(sum_date[:-1])

    # Minutes
    if (increment_size == "n"):
        return date + timedelta(minutes=amount)

    # Hours
    if (increment_size == "h"):
        return date + timedelta(hours=amount)

    # Days
    if (increment_size == "d"):
        return date + timedelta(days=amount)

    # Weeks
    if (increment_size == "w"):
        return date + timedelta(weeks=amount)

    # Month
    if (increment_size == "m"):
        return date + relativedelta(months=amount)

    # Year
    if (increment_size == "y"):
        return date + relativedelta(years=amount)
