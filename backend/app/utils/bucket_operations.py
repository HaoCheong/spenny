from datetime import datetime

# Update a singular bucket value
import app.api.cruds.flow_event_cruds as flow_event_cruds
import app.api.schemas.trigger_schemas as trigger_schemas
import app.utils.trigger_operations as tro
from app.utils.trigger_operations import bring_forward
from app.utils.helpers import add_time
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def update_all_buckets(db: Session, datetime_bound: datetime = datetime.now()):

    # Get all Flow Events
    all_flowEvents = flow_event_cruds.get_all_flowEvents(db=db)

    for fe in all_flowEvents:
        # PFIX: Why the fuck is this necessary for thr next trigger to carry forward v
        access: str = fe.id

        # Jsonably encode the flowevent to something readable
        curr_fe = jsonable_encoder(fe)

        # Get the next trigger date
        curr_next_trigger = datetime.strptime(
            curr_fe['next_trigger'].split(".")[0], "%Y-%m-%dT%H:%M:%S")

        # If the baounding datetime (defaulted to now) is before the trigger, skip to next FE
        if (datetime_bound <= curr_next_trigger):
            continue

        # Continually loop through until next trigger passes the bound date
        while curr_next_trigger < datetime_bound:
            print("CURR_NEXT_TRIGGER", curr_next_trigger)

            bring_forward_details = trigger_schemas.BringForwardBase(
                money_include=True,
                flow_event_id=curr_fe['id']
            )

            bring_forward(details=bring_forward_details, db=db)

            curr_fe = jsonable_encoder(
                flow_event_cruds.get_flowEvent_by_id(db=db, id=curr_fe['id']))

            curr_next_trigger = datetime.strptime(
                curr_fe['next_trigger'].split(".")[0], "%Y-%m-%dT%H:%M:%S")
