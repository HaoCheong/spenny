import cruds
import json
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from database import SessionLocal, engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

