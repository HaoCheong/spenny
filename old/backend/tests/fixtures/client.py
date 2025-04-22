'''client_fixture.py

Contains all the necessary processes to create a sqlalchemy compatible testing client
'''

from app.database.database import Base
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
import os

import pytest

from app.helpers import get_db
from app.main import app

import pathlib

# Creates an initial engine that does point to production
ABS_PATH = pathlib.Path().resolve()
POSTGRES_DATABASE_URL = f"postgresql://{os.environ.get('SPENNY_DB_USER')}:{os.environ.get('SPENNY_DB_PASS')}@{os.environ.get('SPENNY_DB_HOST')}:{os.environ.get('SPENNY_DB_PORT')}/{os.environ.get('SPENNY_DB_NAME')}"


engine = create_engine(
    POSTGRES_DATABASE_URL,
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    # Overiddes the database with a testing database
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


@pytest.fixture
def reset_db():
    ''' Resets the database via dropping '''
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
