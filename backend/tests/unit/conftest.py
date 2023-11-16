from app.database import Base
from app.helpers import get_db
from app.main import app

from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
import pytest
from datetime import datetime, timedelta


import pathlib

ABS_PATH = pathlib.Path().resolve()
SQLALCHEMY_DATABASE_URL = f"sqlite:///{ABS_PATH}/app/db/spenny_test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Overiddes the database with a testing database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Overiddes a dependency function with another function
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

SUCCESS = 200
ERROR = 400

def get_days_since_today(days):
    today = str(datetime.now()).split(" ")[0]
    today_midnight = datetime.strptime(today, "%Y-%m-%d")
    return today_midnight + timedelta(days=days)

@pytest.fixture
def reset_db():
    ''' Resets the database via dropping '''
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def buckets_data():
    return [
            {
                "name": "Total",
                "description": "Total amount in account",
                "current_amount": 10000.0,
                "properties": {
                    "invisible": False
                }
            },
            {
                "name": "Savings",
                "description": "General Savings",
                "current_amount": 5000.0,
                "properties": {
                    "invisible": False
                }
            },
            {
                "name": "Household",
                "description": "Fund for household requirements",
                "current_amount": 1000.0,
                "properties": {
                    "invisible": False
                }
            },
            {
                "name": "Lifestyle",
                "description": "For the week by week spending",
                "current_amount": 1000.0,
                "properties": {
                    "invisible": False
                }
            },
            {
                "name": "Food",
                "description": "Food spending",
                "current_amount": 500.0,
                "properties": {
                    "invisible": False
                }
            },
            {
                "name": "Fun",
                "description": "Fun spending",
                "current_amount": 200.0,
                "properties": {
                    "invisible": False
                }
            }
        ]

@pytest.fixture
def flow_events_data():
    return [
        {
            "name": "Main Job income",
            "description": "My main salary",
            "change_amount": 5000.0,
            "type": "ADD",
            "frequency": "1m",
            "from_bucket_id": None,
            "to_bucket_id": 1,
            "next_trigger": str(get_days_since_today(30))
        },
        {
            "name": "Weekly Lifestyle Move",
            "description": "Automated saving move",
            "change_amount": 240.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 1,
            "to_bucket_id": 4,
            "next_trigger": str(get_days_since_today(7))
        },
        {
            "name": "Gym Spending",
            "description": "For exercise",
            "change_amount": 180.0,
            "type": "SUB",
            "frequency": "1w",
            "from_bucket_id": 1,
            "to_bucket_id": None,
            "next_trigger": str(get_days_since_today(7))
        },
        {
            "name": "Household spending move",
            "description": "Moving Total to household spending",
            "change_amount": 600.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 1,
            "to_bucket_id": 3,
            "next_trigger": str(get_days_since_today(7))
        },
        {
            "name": "Savings Move",
            "description": "Money to be saved on untouched",
            "change_amount": 2000.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 1,
            "to_bucket_id": 2,
            "next_trigger": str(get_days_since_today(7))
        },
        {
            "name": "Weekly Rent Spending",
            "description": "Moving household into rent",
            "change_amount": 560.0,
            "type": "SUB",
            "frequency": "1w",
            "from_bucket_id": 3,
            "to_bucket_id": None,
            "next_trigger": str(get_days_since_today(7))
        },
        {
            "name": "Weekly Utiltity Spending",
            "description": "Electricity + Gas + Internet",
            "change_amount": 160.0,
            "type": "SUB",
            "frequency": "1m",
            "from_bucket_id": 3,
            "to_bucket_id": None,
            "next_trigger": str(get_days_since_today(30))
        },

        {
            "name": "Weekly Food Move",
            "description": "Food funding move",
            "change_amount": 200.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 4,
            "to_bucket_id": 5,
            "next_trigger": str(get_days_since_today(7))
        },
        {
            "name": "Weekly Fun Move",
            "description": "Food funding move",
            "change_amount": 40.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 4,
            "to_bucket_id": 6,
            "next_trigger": str(get_days_since_today(7))
        }
    ]

@pytest.fixture
def logs_data():
    return [
        {
            "name": "Main Job income",
            "description": "My main salary",
            "type": "ADD",
            "amount": 5000,
            "date_created": str(get_days_since_today(60)),
            "bucket_id": 1
        },
        {
            "name": "Gym Spending",
            "description": "For exercise",
            "type": "SUB",
            "amount": 18,
            "date_created": str(get_days_since_today(9)),
            "bucket_id": 1
        },
        {
            "name": "Household spending move",
            "description": "Moving Total to household spending",
            "type": "MOV",
            "amount": 600,
            "date_created": str(get_days_since_today(13)),
            "bucket_id": 1
        },
        {
            "name": "Savings Move",
            "description": "Money to be saved on untouched",
            "type": "MOV",
            "amount": 2000,
            "date_created": str(get_days_since_today(60)),
            "bucket_id": 1
        },
        {
            "name": "Woolies shopping",
            "description": "Friday woolies shopping",
            "type": "SUB",
            "amount": 65,
            "date_created": str(get_days_since_today(3)),
            "bucket_id": 5
        },
        {
            "name": "Eating at Cafe de la Cafe",
            "description": "Brekkie",
            "type": "SUB",
            "amount": 30,
            "date_created": str(get_days_since_today(2)),
            "bucket_id": 5
        },
        {
            "name": "Bought Video Game 2: More games",
            "description": "Let me be happy",
            "type": "SUB",
            "amount": 55,
            "date_created": str(get_days_since_today(1)),
            "bucket_id": 6
        }
    ]

