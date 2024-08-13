from dateutil.relativedelta import relativedelta
from fastapi.encoders import jsonable_encoder

from tests.unit.data_fixtures import *
from tests.unit import wrappers
from tests.unit.client_fixtures import get_test_db

import app.operations.operation_helpers as oph
import app.operations.trigger_operations as tro
import app.operations.bucket_operations as bko

import app.schemas.trigger_schemas as schemas


# ========== Bucket Operations Tests ==========


def test_update_bucket_values(populate_database):
    pass


def test_update_all_buckets(populate_database):
    pass


# ========== Trigger Operations Tests ==========


def test_manual_trigger(populate_database, get_test_db):

    # Get and prepare mocked data
    test_db = get_test_db

    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    test_bucket_to = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(2))['data']

    # Test adding trigger
    test_trigger = {
        "name": f"Test Trigger",
        "description": f"Testing a trigger",
        "change_amount": 100,
        "type": "ADD",
        "from_bucket_id": None,
        "to_bucket_id": test_bucket_to.get("id")
    }

    res = tro.manual_trigger(test_trigger, test_db)
    test_bucket_to = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(2))['data']
    assert test_bucket_to.get("current_amount") == 5100.0
    assert res == {"Success": True}

    # Test Subtraction Trigger
    test_trigger = {
        "name": f"Test Trigger",
        "description": f"Testing a trigger",
        "change_amount": 100,
        "type": "SUB",
        "from_bucket_id": test_bucket_from.get("id"),
        "to_bucket_id": None
    }

    res = tro.manual_trigger(test_trigger, test_db)
    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    assert test_bucket_from.get("current_amount") == 9900.0
    assert res == {"Success": True}

    # Test Subtraction Trigger
    test_trigger = {
        "name": f"Test Trigger",
        "description": f"Testing a trigger",
        "change_amount": 100,
        "type": "MOV",
        "from_bucket_id": test_bucket_from.get('id'),
        "to_bucket_id": test_bucket_to.get("id")
    }

    res = tro.manual_trigger(test_trigger, test_db)
    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    test_bucket_to = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(2))['data']

    assert test_bucket_from.get("current_amount") == 9800.0
    assert test_bucket_to.get("current_amount") == 5200.0
    assert res == {"Success": True}


def test_bring_forward(populate_database, get_test_db):

    test_db = get_test_db
    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    test_flow_event = jsonable_encoder(
        wrappers.get_flow_event_by_flow_event_id(1))['data']
    test_next_trigger = datetime.strptime(
        test_flow_event.get('next_trigger'), "%Y-%m-%dT%H:%M:%S")

    test_bring_forward = schemas.BringForwardBase(
        money_include=False,
        flow_event_id=test_flow_event.get("id")
    )
    print("test_next_trigger 1", test_next_trigger)
    tro.bring_forward(test_bring_forward, test_db)
    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    test_flow_event = jsonable_encoder(
        wrappers.get_flow_event_by_flow_event_id(1))['data']
    assert test_bucket_from.get("current_amount") == 10000.0
    assert datetime.strptime(
        test_flow_event.get('next_trigger'), "%Y-%m-%dT%H:%M:%S") == test_next_trigger + relativedelta(months=1)

    test_bring_forward = schemas.BringForwardBase(
        money_include=True,
        flow_event_id=test_flow_event.get("id")
    )

    # Error: Its doubling the next trigger?
    tro.bring_forward(test_bring_forward, test_db)
    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    test_flow_event = jsonable_encoder(
        wrappers.get_flow_event_by_flow_event_id(1))['data']
    test_next_trigger = datetime.strptime(
        test_flow_event.get('next_trigger'), "%Y-%m-%dT%H:%M:%S")

    print("test_next_trigger 2", test_next_trigger)
    assert test_bucket_from.get("current_amount") == 15000.0
    assert datetime.strptime(
        test_flow_event.get('next_trigger'), "%Y-%m-%dT%H:%M:%S") == test_next_trigger + relativedelta(months=1)

# ========== Operations Helper Tests ==========


def test_change_bucket_value(populate_database, get_test_db):

    # Get and prepare mocked data
    test_db = get_test_db
    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))['data']
    test_amount = 100

    assert test_bucket.get("current_amount") == 10000.0

    # Test that adding works
    res = oph.change_bucket_value(test_bucket, 'ADD', test_amount, test_db)
    assert test_bucket.get("current_amount") == 10100.0

    # Test that subtraction works
    oph.change_bucket_value(test_bucket, 'SUB', test_amount, test_db)
    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))['data']
    assert test_bucket.get("current_amount") == 10000.0

    # Test that adding 0 works
    oph.change_bucket_value(test_bucket, 'ADD', 0, test_db)
    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))['data']
    assert test_bucket.get("current_amount") == 10000.0

    # Test adding negatives should work
    oph.change_bucket_value(test_bucket, 'ADD', -1 * test_amount, test_db)
    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))['data']
    assert test_bucket.get("current_amount") == 9900.0

# ========== OTHER ==========


def test_other(populate_database, get_test_db):

    test_db = get_test_db
    db_buckets = wrappers.get_all_buckets()

    print("DB_BUCKET", db_buckets)
    print("TEST_DB", type(test_db))
    pass
