''' Database

Contains all the configuration variables for creating an engine and a session
- Engine: Establish what SQL DBMS the application is interfacing with
- Session: A connection instance to the DBMS

'''

from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
import os

POSTGRES_DATABASE_URL = f"postgresql://{os.environ.get('SPENNY_POSTGRES_DB_USER')}:{os.environ.get('SPENNY_POSTGRES_DB_PASS')}@{os.environ.get('SPENNY_POSTGRES_DB_HOST')}:{os.environ.get('SPENNY_POSTGRES_DB_PORT')}/{os.environ.get('SPENNY_POSTGRES_DB_NAME')}"

engine = create_engine(POSTGRES_DATABASE_URL)


def create_db_and_tables():
    ''' Instantiate the database tables '''
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
