from dateutil.relativedelta import relativedelta
from fastapi.encoders import jsonable_encoder

from tests.data_fixtures import *
from tests.unit import wrappers
from tests.client_fixtures import get_test_db

import app.operations.operation_helpers as oph
import app.operations.trigger_operations as tro
import app.operations.bucket_operations as bko

import app.api.schemas.trigger_schemas as schemas


# ========== Bucket Operations Tests ==========


def test_update_all_buckets(populate_database, get_test_db):

    # Get and prepare mocked data
    test_db = get_test_db
    test_datetime = datetime(2024, 6, 23, 0, 0, 0, 0)

    # test_all_buckets = wrappers.get_all_buckets()['data']
    # for tb in test_all_buckets:
    #     print("PRE - ", tb)

    test_flow_events = wrappers.get_all_flow_events()['data']
    for tfe in test_flow_events:
        pre_time = datetime.strptime(tfe['next_trigger'], "%Y-%m-%dT%H:%M:%S")
        assert pre_time < test_datetime

    bko.update_all_buckets(test_db, test_datetime)

    # test_all_buckets = wrappers.get_all_buckets()['data']
    # for tb in test_all_buckets:
    #     print("POST - ", tb)

    test_flow_events = wrappers.get_all_flow_events()['data']
    for tfe in test_flow_events:
        post_time = datetime.strptime(tfe['next_trigger'], "%Y-%m-%dT%H:%M:%S")
        assert post_time >= test_datetime


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

    # Get and prepare mock data
    test_db = get_test_db
    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    test_flow_event = jsonable_encoder(
        wrappers.get_flow_event_by_flow_event_id(1))['data']
    test_next_trigger = datetime.strptime(
        test_flow_event.get('next_trigger'), "%Y-%m-%dT%H:%M:%S")

    # Test Valid Case exclusive of bringing money forward
    test_bring_forward = schemas.BringForwardBase(
        money_include=False,
        flow_event_id=test_flow_event.get("id")
    )

    tro.bring_forward(test_bring_forward, test_db)
    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    test_flow_event = jsonable_encoder(
        wrappers.get_flow_event_by_flow_event_id(1))['data']

    assert test_bucket_from.get("current_amount") == 10000.0
    assert datetime.strptime(
        test_flow_event.get('next_trigger'), "%Y-%m-%dT%H:%M:%S") == test_next_trigger + relativedelta(months=1)

    # Test Valid Case inclusive of bringing money forward
    test_next_trigger = datetime.strptime(
        test_flow_event.get('next_trigger'), "%Y-%m-%dT%H:%M:%S")
    test_bring_forward = schemas.BringForwardBase(
        money_include=True,
        flow_event_id=test_flow_event.get("id")
    )

    tro.bring_forward(test_bring_forward, test_db)
    test_bucket_from = jsonable_encoder(
        wrappers.get_bucket_by_bucket_id(1))['data']
    test_flow_event = jsonable_encoder(
        wrappers.get_flow_event_by_flow_event_id(1))['data']

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
    oph.change_bucket_value(test_bucket, 'ADD', test_amount, test_db)
    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))['data']
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

    oph.change_bucket_value(test_bucket, 'MULT', 0.1, test_db)
    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))['data']
    assert test_bucket.get("current_amount") == 10890.0

    oph.change_bucket_value(test_bucket, 'MULT', -0.1, test_db)
    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))['data']
    assert test_bucket.get("current_amount") == 9801.0