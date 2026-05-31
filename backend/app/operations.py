from datetime import datetime, timezone
from pydantic import TypeAdapter
from sqlalchemy import true
from sqlalchemy.orm import Session

from app.helpers import event_freq_adder
import app.cruds.bucket_cruds as bucket_cruds
from app.domain.event.operation_domain import Operation
from app.domain.event.money.transfer_money_operations_domain import TranferMoneyOperation
from app.domain.event.trigger_domain import TimedTrigger, Trigger
import app.cruds.event_cruds as event_cruds
from app.models.event_models import Event
import app.domain.event.event_domain as event_schemas
import app.domain.log.log_schemas as log_schemas
import app.cruds.log_cruds as log_cruds
import app.models.bucket_models as bucket_modals

_operation_adapter = TypeAdapter(Operation)

# PFIX: Maybe a return for FE reactivity sake? Later
def run_manual_entry(db: Session, entry: event_schemas.ManualActionBase, entry_datetime: datetime = datetime.now(timezone.utc)):

    op = entry.operation

    # PFIX: Perhaps a delegation pattern/layer applied to this step would be better on a maintainability perspective
    # PFIX: Duplicated code and thus can be adjusted
    # PFIX: Will need to duplicate the logging code here for now as well
    if isinstance(op, TranferMoneyOperation):
        from_bucket = bucket_cruds.get_bucket_by_id(db, entry.bucket_id)
        to_bucket = bucket_cruds.get_bucket_by_id(db, op.to_bucket_id)
        op.apply(to_bucket, from_bucket)
        db.add(from_bucket)
        db.add(to_bucket)

        # PFIX: This is a hack to get the type checking through, should enforce with an error
        assert isinstance(from_bucket, bucket_modals.Bucket)
        assert isinstance(to_bucket, bucket_modals.Bucket)

        # PFIX: Could probably create a service that does this instead?
        # PFIX: Event properties not having a clean typing is kinda ass?
        # PFIX: Perhaps add the onus of logging, or logging construction to the operation and trigger class?
        # Logs the FROM bucket
        log_cruds.create_log(db=db, log=log_schemas.LogCreate(
            bucket_id=from_bucket.id,
            bucket_name=from_bucket.name,
            bucket_description=from_bucket.description,
            event_id=None,
            action_name=entry.name,
            action_description=entry.name,
            action_properties={
                "trigger": entry.trigger.model_dump(mode="json"),
                "operation": entry.operation.model_dump(mode="json"),
            },
            created_at=entry_datetime,
            updated_at=entry_datetime
        ))

        # Logs the TO Bucket
        log_cruds.create_log(db=db, log=log_schemas.LogCreate(
            bucket_id=to_bucket.id,
            bucket_name=to_bucket.name,
            bucket_description=to_bucket.description,
            event_id=None,
            action_name=entry.name,
            action_description=entry.name,
            action_properties={
                "trigger": entry.trigger.model_dump(mode="json"),
                "operation": entry.operation.model_dump(mode="json"),
            },
            created_at=entry_datetime,
            updated_at=entry_datetime
        ))
        
    else:
        bucket = bucket_cruds.get_bucket_by_id(db, entry.bucket_id)
        op.apply(bucket)
        db.add(bucket)

        # PFIX: Another assert hack to trick the typing
        assert isinstance(bucket, bucket_modals.Bucket)

        log_cruds.create_log(db=db, log=log_schemas.LogCreate(
            bucket_id=bucket.id,
            bucket_name=bucket.name,
            bucket_description=bucket.description,
            event_id=None,
            action_name=entry.name,
            action_description=entry.name,
            action_properties={
                "trigger": entry.trigger.model_dump(mode="json"), # PFIX: Will this even work?
                "operation": entry.operation.model_dump(mode="json"), # PFIX: Will this even work?
            },
            created_at=entry_datetime,
            updated_at=entry_datetime
        ))

    

    db.commit()

def run_update(db: Session, update_datetime: datetime = datetime.now(timezone.utc)):

    if update_datetime.tzinfo is None:
        update_datetime = update_datetime.replace(tzinfo=timezone.utc)

    # Grabs all the events up until the current datetime
    # res = event_cruds.get_all_events(db=db, all=True)
    # PFIX: Might need to index on trigger datetime but can you even?
    
    res = event_cruds.get_events_by_date_range(db=db, end_datetime=update_datetime)
    to_process = res["data"]
    
    # Repeat until events list to process is empty
    while to_process:
        
        to_process.sort(key=lambda e: e.trigger.next_trigger_date, reverse=True)
        db_event = to_process.pop(0)

        # Iterates through an event, takes the event type and runs their relevant apply
        # PFIX: What the fuck does this do?
        op = _operation_adapter.validate_python(db_event.operation)

        # PFIX: Perhaps a delegation pattern/layer applied to this step would be better on a maintainability perspective
        if isinstance(op, TranferMoneyOperation):
            from_bucket = bucket_cruds.get_bucket_by_id(db, db_event.bucket_id)
            to_bucket = bucket_cruds.get_bucket_by_id(db, op.to_bucket_id)
            op.apply(to_bucket, from_bucket)
            db.add(from_bucket)
            db.add(to_bucket)

            # PFIX: This is a hack to get the type checking through, should enforce with an error
            assert isinstance(from_bucket, bucket_modals.Bucket)
            assert isinstance(to_bucket, bucket_modals.Bucket)

            log_cruds.create_log(db=db, log=log_schemas.LogCreate(
                bucket_id=from_bucket.id,
                bucket_name=from_bucket.name,
                bucket_description=from_bucket.description,
                event_id=None,
                action_name=db_event.name,
                action_description=db_event.name,
                action_properties={
                    "trigger": db_event.trigger.model_dump(mode="json"),
                    "operation": op.model_dump(mode="json"),
                },
                created_at=db_event.trigger.next_trigger_date, # PFIX: Is this clean, please review
                updated_at=update_datetime
            ))

            # Logs the TO Bucket
            log_cruds.create_log(db=db, log=log_schemas.LogCreate(
                bucket_id=to_bucket.id,
                bucket_name=to_bucket.name,
                bucket_description=to_bucket.description,
                event_id=None,
                action_name=db_event.name,
                action_description=db_event.name,
                action_properties={
                    "trigger": db_event.trigger.model_dump(mode="json"),
                    "operation": op.model_dump(mode="json"),
                },
                created_at=db_event.trigger.next_trigger_date,
                updated_at=update_datetime
            ))

        else:
            bucket = bucket_cruds.get_bucket_by_id(db, db_event.bucket_id)
            op.apply(bucket)
            db.add(bucket)

            # PFIX: Another assert hack to trick the typing
            assert isinstance(bucket, bucket_modals.Bucket)

            log_cruds.create_log(db=db, log=log_schemas.LogCreate(
                bucket_id=bucket.id,
                bucket_name=bucket.name,
                bucket_description=bucket.description,
                event_id=None,
                action_name=db_event.name,
                action_description=db_event.name,
                action_properties={
                    "trigger": db_event.trigger.model_dump(mode="json"), # PFIX: Will this even work?
                    "operation": op.model_dump(mode="json"), # PFIX: Not sure about using op here, feel inconsistent
                },
                created_at=db_event.trigger.next_trigger_date,
                updated_at=update_datetime
            ))

        # Updates the bucket + event trigger date

        new_trigger_date = event_freq_adder(db_event.trigger.next_trigger_date, db_event.trigger.frequency)
        db_event.trigger = db_event.trigger.model_copy(update={"next_trigger_date": new_trigger_date}) # PFIX: Really no better way
        db_event.updated_at = datetime.now(timezone.utc)
        db.add(db_event)
        db.commit()
        db.refresh(db_event)

        # If trigger date is still before update_datetime, append the list
        if db_event.trigger.next_trigger_date < update_datetime:
            to_process.append(db_event)   

    
    return {"success": True}