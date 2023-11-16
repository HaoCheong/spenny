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
                "current_amount": 1800.0,
                "properties": {
                    "invisible": False
                }
            },
            {
                "name": "Lifestyle",
                "description": "Everything from food to fun",
                "current_amount": 200.0,
                "properties": {
                    "invisible": False
                }
            },
            {
                "name": "Food",
                "description": "My crippling eating habits",
                "current_amount": 0.0,
                "properties": {
                    "invisible": False
                }
            },
            {
                "name": "Fun",
                "description": "For my hobbies and fun stuff ",
                "current_amount": 0.0,
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
            "change_amount": 5562.0,
            "type": "ADD",
            "frequency": "5d",
            "from_bucket_id": None,
            "to_bucket_id": 1,
            "next_trigger": get_days_since_today(5)
        },
        {
            "name": "Savings",
            "description": "Automated saving move",
            "change_amount": 1800.0,
            "type": "MOV",
            "frequency": "3d",
            "from_bucket_id": 1,
            "to_bucket_id": 2,
            "next_trigger": get_days_since_today(5)
        },
        {
            "name": "Rent",
            "description": "Purely to live at my apartment",
            "change_amount": 560.0,
            "type": "SUB",
            "frequency": "5d",
            "from_bucket_id": 1,
            "to_bucket_id": None,
            "next_trigger": get_days_since_today(5)
        },
        {
            "name": "Gym",
            "description": "Fitness Finance",
            "change_amount": 18.0,
            "type": "SUB",
            "frequency": "2d",
            "from_bucket_id": 1,
            "to_bucket_id": None,
            "next_trigger": get_days_since_today(5)
        },
        {
            "name": "Lifestyle",
            "description": "Money for actually living in the cruel world",
            "change_amount": 240.0,
            "type": "MOV",
            "frequency": "4d",
            "from_bucket_id": 1,
            "to_bucket_id": 3,
            "next_trigger": get_days_since_today(5)
        },
        {
            "name": "Food",
            "description": "Budget for eating",
            "change_amount": 200.0,
            "type": "MOV",
            "frequency": "3d",
            "from_bucket_id": 3,
            "to_bucket_id": 4,
            "next_trigger": get_days_since_today(5)
        },
        {
            "name": "Fun",
            "description": "Hobby Funding",
            "change_amount": 40.0,
            "type": "MOV",
            "frequency": "1d",
            "from_bucket_id": 3,
            "to_bucket_id": 5,
            "next_trigger": get_days_since_today(5)
        },
    ]

@pytest.fixture
def log_data():
    pass

