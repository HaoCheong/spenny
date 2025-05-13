'''
Service layer for Event
'''

import app.cruds.bucket_cruds as bucket_cruds
import app.cruds.event_cruds as event_cruds
import app.schemas.bucket_schemas as bucket_schemas
import app.schemas.event_schemas as event_schemas

from app.helpers import get_db
from abc import abstractmethod, ABC


class EventExecuter(ABC):

    @abstractmethod
    def execute():
        pass


class EventOperation:

    def _add_event(EventExecuter):
        pass

    def _sub_event(EventExecuter):
        pass

    def _move_event(EventExecuter):
        pass

    def _mult_event(EventExecuter):
        pass

    def _cmv_event(EventExecuter):
        pass

    def execute_event(event: event_schemas.EventReadNR, exec_func):
        ''' Execute a single event'''

        # Determine the event type

        # Given the event type, pass in the required event structure

        #
        pass

    def update_all_events(self):
        ''' Execute all the events and update them '''

        # Get all events

        db = get_db()
        event_data = event_cruds.get_all_events(db=db, skip=0, limit=1)
        all_events_data = event_cruds.get_all_events(
            db=db, skip=0, limit=event_data.total)
        all_events = all_events_data.data

        # Iterate over all events
        for event in all_events:
            if event.event_type == "ADD":
                self.execute_event(event, self._add_event)
            elif event.event_type == "SUB":
                self.execute_event(event, self._sub_event)
            elif event.event_type == "MOV":
                self.execute_event(event, self._add_event)
            elif event.event_type == "MULT":
                self.execute_event(event, self._add_event)
            elif event.event_type == "CMV":
                self.execute_event(event, self._add_event)
            else:
                pass
