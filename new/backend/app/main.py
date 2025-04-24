''' Main File

Calls and initialises the application.
Endpoints and CRUDs are all split based on the associated SQL table.

'''

from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session

import app.endpoints.event_endpoints as event_endpoints
import app.endpoints.bucket_endpoints as bucket_endpoints
import app.metadata as metadata
from app.database.database import create_db_and_tables

app = FastAPI(
    openapi_tags=metadata.tags_metadata,
    title=metadata.app_title,
    description=metadata.app_desc,
    version=metadata.app_version
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return { "connection": True }

app.include_router(event_endpoints.router)
app.include_router(bucket_endpoints.router)