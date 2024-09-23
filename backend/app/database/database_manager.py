
"""Database.py

Controls all the creation of the database

Terms:
 - SQLALCHEMY_DATABASE_URL: Location of the database (SQLITE3 in this case)
 - engine: Create a connection to the database
 - SessionLocal: A local instance of the database
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pathlib
# from configs.config_manager import config
from app.configs.config_manager import config

ABS_PATH = pathlib.Path().resolve()
SQLALCHEMY_DATABASE_URL = f"sqlite:////{ABS_PATH}/app/database/{config.get_config()['DB_FILE_NAME']}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
