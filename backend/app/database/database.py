import pathlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

# Grabs the absolute path of this files location
# Thus making this code agnostic to whatever file structure you are on
ABS_PATH = pathlib.Path().resolve()
POSTGRES_DATABASE_URL = f"postgresql://{os.environ.get('SPENNY_DB_USER')}:{os.environ.get('SPENNY_DB_PASS')}@{os.environ.get('SPENNY_DB_HOST')}:{os.environ.get('SPENNY_DB_PORT')}/{os.environ.get('SPENNY_DB_NAME')}"

engine = create_engine(
    POSTGRES_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
