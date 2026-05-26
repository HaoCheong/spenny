from datetime import datetime, timezone
from pydantic import TypeAdapter
from sqlalchemy import true
from sqlalchemy.orm import Session

from app.helpers import event_freq_adder
import app.cruds.bucket_cruds as bucket_cruds
from app.domain.event.operation_domain import Operation
from app.domain.event.money.transfer_money_operations_domain import TranferMoneyOperation
from app.domain.event.trigger_domain import TimedTrigger
import app.cruds.event_cruds as event_cruds
from app.models.event_models import Event
from app.domain.event.event_domain import EventReadNR


_operation_adapter = TypeAdapter(Operation)



def run_update(db: Session, update_datetime: datetime = datetime.now(timezone.utc)):

    if update_datetime.tzinfo is None:
        update_datetime = update_datetime.replace(tzinfo=timezone.utc)

    # Grabs all the events up until the current datetime
    # res = event_cruds.get_all_events(db=db, all=True)
    res = event_cruds.get_events_by_date_range(db=db, end_datetime=update_datetime)
    to_process = res["data"]
    
    # Repeat until events list to process is empty
    while to_process:
        
        to_process.sort(key=lambda e: e.trigger.next_trigger_date, reverse=True)
        db_event = to_process.pop(0)

        # Iterates through an event, takes the event type and runs their relevant apply
        # PFIX: What the fuck does this do?
        op = _operation_adapter.validate_python(db_event.operation)

        if isinstance(op, TranferMoneyOperation):
            from_bucket = bucket_cruds.get_bucket_by_id(db, db_event.bucket_id)
            to_bucket = bucket_cruds.get_bucket_by_id(db, op.to_bucket_id)
            op.apply(to_bucket, from_bucket)
            db.add(from_bucket)
            db.add(to_bucket)
        else:
            bucket = bucket_cruds.get_bucket_by_id(db, db_event.bucket_id)
            op.apply(bucket)
            db.add(bucket)

        # Updates the bucket + event trigger date

        new_trigger_date = event_freq_adder(db_event.trigger.next_trigger_date, db_event.trigger.frequency)
        db_event.trigger = db_event.trigger.model_copy(update={"next_trigger_date": new_trigger_date}) # PFIX: Really no better way
        db_event.updated_at = datetime.now(timezone.utc)
        db.add(db_event)
        db.commit()
        db.refresh(db_event)

        # print(f"next_trigger_date: {db_event.trigger['next_trigger_date']} | tzinfo: {db_event.trigger['next_trigger_date'].tzinfo}")
        # print(f"update_datetime: {update_datetime} | tzinfo: {update_datetime.tzinfo}")

        # If trigger date is still before update_datetime, append the list
        if db_event.trigger.next_trigger_date < update_datetime:
            to_process.append(db_event)   

    
    return {"success": True}