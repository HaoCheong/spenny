from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import app.metadata as metadata
import app.database as database

from app.database import engine

import app.endpoints.operation_endpoints as operation_endpoints
import app.endpoints.bucket_endpoints as bucket_endpoints
import app.endpoints.flow_event_endpoints as flow_event_endpoints
import app.endpoints.log_endpoints as log_endpoints

database.Base.metadata.create_all(bind=engine)

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

# ======== ROOT ENDPOINT ========
# Not necessary but good indication that connection been made

@app.get("/")
def root():
    return {"connection": True}

app.include_router(operation_endpoints.router)
app.include_router(bucket_endpoints.routers)
app.include_router(flow_event_endpoints.routers)
app.include_router(log_endpoints.routers)

