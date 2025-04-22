"""main.py (5)

Where the endpoints are instantiated and functions are called

- All the data validation are checked here
- Error raising done on this level

"""

from fastapi import FastAPI

import app.database.database as database
import app.metadata as metadata

from app.database.database import engine
from fastapi.middleware.cors import CORSMiddleware

import app.endpoints.bucket_endpoints as bucket_endpoints
import app.endpoints.event_endpoints as event_endpoints
import app.endpoints.assignment_endpoints as assignment_endpoints
import app.endpoints.log_endpoints as log_endpoints
from app.operations.event_operations import EventOperation
from sqlalchemy.orm import Session
from fastapi import Depends
from app.helpers import get_db

database.Base.metadata.create_all(bind=engine)


# Initialising instance of the backend
app = FastAPI(
    openapi_tags=metadata.tags_metadata,
    swagger_ui_parameters=metadata.swagger_ui_parameters,
    title=metadata.app_title,
    description=metadata.app_desc,
    version=metadata.app_version,
)

# Handles CORS, currently available to any origin. Need to be tweaked for security
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======== ROOT ENDPOINT ========
# Not necessary but good indication that connection been made


@app.get("/")
def root():
    return {"connection": True}


@app.get("/call")
def call(db: Session = Depends(get_db)):
    return {"Call": True}


app.include_router(assignment_endpoints.router)
app.include_router(bucket_endpoints.router)
app.include_router(event_endpoints.router)
app.include_router(log_endpoints.router)
