from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import cruds
import models
import schemas
import endpoints
import metadata
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

# Initialising instance of the backend
app = FastAPI(title="Spenny", openapi_tags=metadata.tags_metadata)

# Handles CORS, currently available to any origin. Need to be tweaked for security
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gets an instance of the DB, will close connection with DB when done


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======== ROOT ENDPOINT ========
# Not necessary but good indication that connection been made


@app.get("/")
def root():
    return {"connection": True}


app.include_router(endpoints.router)
