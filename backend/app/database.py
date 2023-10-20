from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pathlib

ABS_PATH = pathlib.Path().resolve()
SQLALCHEMY_DATABASE_URL = f"sqlite:///{ABS_PATH}/app/db/spenny_test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
