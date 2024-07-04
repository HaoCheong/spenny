from app.database import Base
from app.helpers import get_db, get_config
from app.main import app

from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
import pytest
from datetime import datetime, timedelta

import pathlib

config = get_config()
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
