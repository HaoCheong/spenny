'''
Service layer for Event
'''

import app.cruds.bucket_cruds as bucket_cruds
import app.cruds.event_cruds as event_cruds

import app.models.bucket_models as bucket_models
import app.models.event_models as event_models

import app.schemas.bucket_schemas as bucket_schemas
import app.schemas.event_schemas as event_schemas

from sqlalchemy.orm import Session
from app.helpers import get_db, event_freq_adder
from abc import abstractmethod, ABC
from datetime import datetime, timedelta


class EventStrategy(ABC):
    ''' Event Strategy Base Class '''

    @abstractmethod
    def execute(self, db: Session, event: event_models.Event, bucket: bucket_models.Bucket) -> list[bucket_models.Bucket]:
        pass


# ==================== Concreate Strategies ====================


class AddStrategy(EventStrategy):

    def execute(db: Session, event: event_schemas.EventReadWR, bucket: bucket_models.Bucket) -> list[bucket_models.Bucket]:
        print("========== EXECUTING ADD ==========")

        add_amount = event.properties.get("amount")
        setattr(bucket, "amount", bucket.amount + add_amount)
        return [bucket]


class SubStrategy(EventStrategy):

    def execute(db: Session, event: event_schemas.EventReadWR, bucket: bucket_models.Bucket) -> list[bucket_models.Bucket]:
        print("========== EXECUTING SUB ==========")

        sub_amount = event.properties.get("amount")
        setattr(bucket, "amount", bucket.amount - sub_amount)
        return [bucket]


class MovStrategy(EventStrategy):
    def execute(db: Session, event: event_schemas.EventReadWR, bucket: bucket_models.Bucket) -> list[bucket_models.Bucket]:
        print("========== EXECUTING MOV ==========")

        from_bucket = bucket
        to_bucket = bucket_cruds.get_bucket_by_id(
            db=db, id=event.properties.get("to_bucket_id"))
        move_amount = event.properties.get("amount")

        setattr(from_bucket, "amount", from_bucket.amount - move_amount)
        setattr(to_bucket, "amount", to_bucket.amount + move_amount)
        return [from_bucket, to_bucket]


class MultStrategy(EventStrategy):
    def execute(db: Session, event: event_schemas.EventReadWR, bucket: bucket_models.Bucket) -> list[bucket_models.Bucket]:
        print("========== EXECUTING MULT ==========")

        from_bucket = bucket
        perc_increase = event.properties.get("percentage")
        new_amount = from_bucket.amount * (1 + perc_increase)

        setattr(from_bucket, "amount", new_amount)

        return [from_bucket]


class CMVStrategy(EventStrategy):
    def execute(db: Session, event: event_schemas.EventReadWR, bucket: bucket_models.Bucket) -> list[bucket_models.Bucket]:
        print("========== EXECUTING CMV ==========")

        from_bucket = bucket
        to_bucket = bucket_cruds.get_bucket_by_id(
            db=db, id=event.properties.get("to_bucket_id"))

        setattr(to_bucket, "amount", to_bucket.amount + from_bucket.amount)
        setattr(from_bucket, "amount", 0)

        return [from_bucket, to_bucket]

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

    def execute_event(self, event: event_schemas.EventReadNR) -> event_schemas.EventReadNR | None:
        ''' Execute a single event'''

        # Grab the full context of the event
        db_event = event_cruds.get_event_by_id(db=self._session, id=event.id)

        # Execute the bucket, returns list of bucket model objects, use the DB session to update and refresh
        affected_db_buckets = self._event_strat.execute(
            self._session, db_event, db_event.bucket)

        for bucket in affected_db_buckets:
            setattr(bucket, "updated_at", datetime.now())
            self._session.add(bucket)
            self._session.commit()

        # Update the event trigger date
        setattr(db_event, "trigger_datetime", event_freq_adder(
            db_event.trigger_datetime, db_event.frequency))
        setattr(db_event, "updated_at", datetime.now())

        self._session.add(db_event)
        self._session.commit()
        self._session.refresh(db_event)

        # Log the execution

        # Return the event as EventReadNR with new trigger date
        return event_schemas.EventReadNR.model_validate(db_event)


class EventOperation:

    @staticmethod
    def event_sort_key(event: event_schemas.EventReadNR):
        event_priority = {
            "ADD": 1,
            "SUB": 1,
            "MOVE": 1,
            "MULT": 0,
            "CMV": 1
        }
        event_priority_score = event_priority.get(event.event_type, 2)

        return (event.trigger_datetime, event_priority_score)

    @staticmethod
    def update_all_events(db, curr_datetime=datetime.now()):
        ''' Execute all the events and update them '''

        # Get all events in the database
        all_events_data = event_schemas.EventAllRead.model_validate(event_cruds.get_all_events(
            db=db, skip=0, limit=1, all=True))
        event_queue = all_events_data.data

        # ========== TEST ==========
        event_queue = event_queue
        # Set up the strategy context
        event_context = EventContext(None, db)

        # Execute until the queue is empty
        while len(event_queue) != 0:

            # Sort the queue via trigger date, from furthest to recent
            event_queue = sorted(
                event_queue, key=EventOperation.event_sort_key)

            # Pop the most recent / prioritised
            event = event_queue.pop()

            if event.event_type == "ADD":
                event_context.event_strat = AddStrategy
            elif event.event_type == "SUB":
                event_context.event_strat = SubStrategy
            elif event.event_type == "MOVE":
                event_context.event_strat = MovStrategy
            elif event.event_type == "MULT":
                event_context.event_strat = MultStrategy
            elif event.event_type == "CMV":
                event_context.event_strat = CMVStrategy
            else:
                raise ValueError(
                    f"Event Type {event.event_type} is not recognised")

            # Execute the event given the context
            next_event = event_context.execute_event(event)

            # If the next event is valid and prior to the curr_datetime
            if next_event and next_event.trigger_datetime < curr_datetime:
                event_queue.append(next_event)
