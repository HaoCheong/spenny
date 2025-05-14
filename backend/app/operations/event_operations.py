'''
Service layer for Event
'''

import app.cruds.bucket_cruds as bucket_cruds
import app.cruds.event_cruds as event_cruds
import app.schemas.bucket_schemas as bucket_schemas
import app.schemas.event_schemas as event_schemas

from sqlalchemy.orm import Session
from app.helpers import get_db
from abc import abstractmethod, ABC


class EventStrategy(ABC):
    ''' Event Strategy Base Class '''

    @abstractmethod
    def execute(self, event, bucket):
        pass

# ==================== Concreate Strategies ====================


class AddStrategy(EventStrategy):

    def execute(self, event, bucket):

        print("EVENT", event)
        print("BUCKET", bucket)
        # Take the amount as per the property in the event

        # Add it to the total

        # Update via b
        pass


class SubStrategy(EventStrategy):
    def execute(self, event, bucket):
        pass


class MovStrategy(EventStrategy):
    def execute(self, event, bucket):
        pass


class MultStrategy(EventStrategy):
    def execute(self, event, bucket):
        pass


class CMVStrategy(EventStrategy):
    def execute(self, event, bucket):
        pass

# ==================== Client Interface/context ====================


class EventContext:

    def __init__(self, event_strat: EventStrategy | None, db: Session):
        self._event_strat = event_strat
        self._session = db

    @property
    def event_strat(self):
        return self._event_strat

    @event_strat.setter
    def event_strat(self, new_strat: EventStrategy):
        self._event_strat = new_strat

    def execute_event(self, event: event_schemas.EventReadNR):
        ''' Execute a single event'''

        # Grab the bucket involve with the event
        bucket = bucket_cruds.get_bucket_by_id(
            db=self._session, id=event.bucket_id)

        print("EVENT", event)
        print("BUCKET", bucket)

        res = self._event_strat.execute(event, bucket)


class EventOperation:

    @staticmethod
    def update_all_events(db):
        ''' Execute all the events and update them '''

        # Get all events
        event_data = event_schemas.EventAllRead(
            **event_cruds.get_all_events(db=db, skip=0, limit=1))
        print("event_data", event_data)
        all_events_data = event_schemas.EventAllRead(**event_cruds.get_all_events(
            db=db, skip=0, limit=event_data.total))
        all_events = all_events_data.data

        event_context = EventContext(None, db)

        # Iterate over all events
        for event in all_events:
            if event.event_type == "ADD":
                event_context.event_strat = AddStrategy
            elif event.event_type == "SUB":
                event_context.event_strat = SubStrategy
            elif event.event_type == "MOV":
                event_context.event_strat = MovStrategy
            elif event.event_type == "MULT":
                event_context.event_strat = MultStrategy
            elif event.event_type == "CMV":
                event_context.event_strat = CMVStrategy
            else:
                raise ValueError(
                    f"Event Type {event.event_type} is not recognised")

            # Execute the event given the context
            event_context.execute_event(event)
