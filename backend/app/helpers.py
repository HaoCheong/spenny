from app.database.database import SessionLocal
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Gets an instance of the DB, will close connection with DB when done


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def event_freq_adder(date_to_change: datetime, event_freq: str) -> datetime:
    freq_qty = int(event_freq[0])
    freq_type = event_freq[1]
    print("PRE DATETIME", date_to_change, freq_qty, freq_type)
    new_datetime = None
    if freq_type == "h":
        new_datetime = date_to_change + relativedelta(hours=freq_qty)
    elif freq_type == "d":
        new_datetime = date_to_change + relativedelta(days=freq_qty)
    elif freq_type == "w":
        new_datetime = date_to_change + relativedelta(weeks=freq_qty)
    elif freq_type == "m":
        new_datetime = date_to_change + relativedelta(months=freq_qty)
    elif freq_type == "y":
        new_datetime = date_to_change + relativedelta(years=freq_qty)
    else:
        raise ValueError(
            f"Frequency Type of '{freq_type}' does not exist.")

    print("POST DATETIME", new_datetime)
    return new_datetime
