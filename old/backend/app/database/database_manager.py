
"""Database.py

Controls all the creation of the database

Terms:
 - SQLALCHEMY_DATABASE_URL: Location of the database (SQLITE3 in this case)
 - engine: Create a connection to the database
 - SessionLocal: A local instance of the database
"""

import os
import pathlib

# from app.configs.config_manager import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ABS_PATH = pathlib.Path().resolve()
POSTGRES_DATABASE_URL = f"postgresql://{os.environ.get('SPENNY_DB_USER')}:{os.environ.get('SPENNY_DB_PASS')}@{os.environ.get('SPENNY_DB_HOST')}:{os.environ.get('SPENNY_DB_PORT')}/{os.environ.get('SPENNY_DB_NAME')}"

engine = create_engine(POSTGRES_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
