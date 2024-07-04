
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
import yaml
import pathlib
import re


def get_config():
    config = None
    ABS_PATH = pathlib.Path().resolve()
    with open(f'{ABS_PATH}/app/spenny_backend_config.yml', encoding='utf-8') as c:
        config = yaml.safe_load(c)
        return config


def get_db():
    from app.database import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_time(date: datetime, sum_date: str) -> datetime:
    '''
    Add a given frequency to a given datetime
    - n: minutes
    - h: hours
    - d: days
    - m: months
    - y: years
    '''

    # Check if sum_date format is correct
    if (re.match(r"^[0-9]+[(n|h|d|m|y)]{1}$", sum_date) is None):
        print("Sum Date does not match expected format: <freq><incr>")
        return None

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
