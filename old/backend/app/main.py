from typing import List

import app.api.endpoints.bucket_endpoints as bucket_endpoints
import app.api.endpoints.flow_event_endpoints as flow_event_endpoints
import app.api.endpoints.log_endpoints as log_endpoints
import app.api.endpoints.operation_endpoints as operation_endpoints
import app.database.database_manager as database
import app.metadata as metadata
from app.database.database_manager import engine
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/heartbeat")
def root():
    return {"connection": True}

app.include_router(operation_endpoints.router, prefix="/api/v1")
app.include_router(bucket_endpoints.router, prefix="/api/v1")
app.include_router(flow_event_endpoints.router, prefix="/api/v1")
app.include_router(log_endpoints.router, prefix="/api/v1")

