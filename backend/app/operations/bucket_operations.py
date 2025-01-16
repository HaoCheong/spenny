from datetime import datetime
from app.utils.helpers import add_time
from app.operations.trigger_operations import bring_forward

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

# Update a singular bucket value
import app.api.cruds.flow_event_cruds as flow_event_cruds
import app.api.schemas.trigger_schemas as trigger_schemas
import app.operations.trigger_operations as tro

def update_all_buckets(db: Session, datetime_bound: datetime = datetime.now()):

    # Get all Flow Events
    all_flowEvents = flow_event_cruds.get_all_flowEvents(db=db)

    for fe in all_flowEvents:
        # PFIX: Why the fuck is this necessary for thr next trigger to carry forward v
        access: str = fe.id
        curr_fe = jsonable_encoder(fe)
        curr_next_trigger = datetime.strptime(
            curr_fe['next_trigger'], "%Y-%m-%dT%H:%M:%S")

        if (datetime_bound <= curr_next_trigger):
            continue

        while curr_next_trigger < datetime_bound:

            bring_forward_details = trigger_schemas.BringForwardBase(
                money_include=True,
                flow_event_id=curr_fe['id']
            )

            bring_forward(details=bring_forward_details, db=db)

            curr_fe = jsonable_encoder(
                flow_event_cruds.get_flowEvent_by_id(db=db, id=curr_fe['id']))

            curr_next_trigger = datetime.strptime(
                curr_fe['next_trigger'], "%Y-%m-%dT%H:%M:%S")
