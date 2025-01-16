import pytest
from datetime import datetime, timedelta
from typing import Optional
from tests.client_fixtures import reset_db

def get_days_since_today(days) -> datetime:
    today = str(datetime.now()).split(" ")[0]
    today_midnight = datetime.strptime(today, "%Y-%m-%d")
    return today_midnight + timedelta(days=days)


def get_test_date(days: int, test_date: Optional[datetime] = None) -> datetime:
    if test_date is not None:
        return test_date

    today = str(datetime.now()).split(" ")[0]
    today_midnight = datetime.strptime(today, "%Y-%m-%d")
    return today_midnight + timedelta(days=days)


@pytest.fixture
def buckets_data():
    return [
        {
            "name": "Total",
            "description": "Total amount in account",
            "current_amount": 10000.0,
            "properties": {
                    "invisible": False
            }
        },
        {
            "name": "Savings",
            "description": "General Savings",
            "current_amount": 5000.0,
            "properties": {
                    "invisible": False
            }
        },
        {
            "name": "Household",
            "description": "Fund for household requirements",
            "current_amount": 1000.0,
            "properties": {
                    "invisible": False
            }
        },
        {
            "name": "Lifestyle",
            "description": "For the week by week spending",
            "current_amount": 1000.0,
            "properties": {
                    "invisible": False
            }
        },
        {
            "name": "Food",
            "description": "Food spending",
            "current_amount": 500.0,
            "properties": {
                    "invisible": False
            }
        },
        {
            "name": "Fun",
            "description": "Fun spending",
            "current_amount": 200.0,
            "properties": {
                    "invisible": False
            }
        }
    ]


@pytest.fixture
def flow_events_data():
    return [
        {
            "name": "Main Job income",
            "description": "My main salary",
            "change_amount": 5000.0,
            "type": "ADD",
            "frequency": "1m",
            "from_bucket_id": None,
            "to_bucket_id": 1,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        },
        {
            "name": "Weekly Lifestyle Move",
            "description": "Automated saving move",
            "change_amount": 240.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 1,
            "to_bucket_id": 4,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        },
        {
            "name": "Gym Spending",
            "description": "For exercise",
            "change_amount": 180.0,
            "type": "SUB",
            "frequency": "1w",
            "from_bucket_id": 1,
            "to_bucket_id": None,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        },
        {
            "name": "Household spending move",
            "description": "Moving Total to household spending",
            "change_amount": 600.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 1,
            "to_bucket_id": 3,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        },
        {
            "name": "Savings Move",
            "description": "Money to be saved on untouched",
            "change_amount": 2000.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 1,
            "to_bucket_id": 2,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        },
        {
            "name": "Weekly Rent Spending",
            "description": "Moving household into rent",
            "change_amount": 560.0,
            "type": "SUB",
            "frequency": "1w",
            "from_bucket_id": 3,
            "to_bucket_id": None,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        },
        {
            "name": "Weekly Utiltity Spending",
            "description": "Electricity + Gas + Internet",
            "change_amount": 160.0,
            "type": "SUB",
            "frequency": "1m",
            "from_bucket_id": 3,
            "to_bucket_id": None,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        },

        {
            "name": "Weekly Food Move",
            "description": "Food funding move",
            "change_amount": 200.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 4,
            "to_bucket_id": 5,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        },
        {
            "name": "Weekly Fun Move",
            "description": "Food funding move",
            "change_amount": 40.0,
            "type": "MOV",
            "frequency": "1w",
            "from_bucket_id": 4,
            "to_bucket_id": 6,
            "next_trigger": str(get_test_date(0, datetime(2024, 6, 6, 0, 0, 0, 0)))
        }
    ]


@pytest.fixture
def logs_data():
    return [
        {
            "name": "Main Job income",
            "description": "My main salary",
            "type": "ADD",
            "amount": 5000,
            "date_created": str(get_days_since_today(60)),
            "bucket_id": 1
        },
        {
            "name": "Gym Spending",
            "description": "For exercise",
            "type": "SUB",
            "amount": 18,
            "date_created": str(get_days_since_today(9)),
            "bucket_id": 1
        },
        {
            "name": "Household spending move",
            "description": "Moving Total to household spending",
            "type": "MOV",
            "amount": 600,
            "date_created": str(get_days_since_today(13)),
            "bucket_id": 1
        },
        {
            "name": "Savings Move",
            "description": "Money to be saved on untouched",
            "type": "MOV",
            "amount": 2000,
            "date_created": str(get_days_since_today(60)),
            "bucket_id": 1
        },
        {
            "name": "Woolies shopping",
            "description": "Friday woolies shopping",
            "type": "SUB",
            "amount": 65,
            "date_created": str(get_days_since_today(3)),
            "bucket_id": 5
        },
        {
            "name": "Eating at Cafe de la Cafe",
            "description": "Brekkie",
            "type": "SUB",
            "amount": 30,
            "date_created": str(get_days_since_today(2)),
            "bucket_id": 5
        },
        {
            "name": "Bought Video Game 2: More games",
            "description": "Let me be happy",
            "type": "SUB",
            "amount": 55,
            "date_created": str(get_days_since_today(1)),
            "bucket_id": 6
        }
    ]


@pytest.fixture
def populate_database(reset_db, flow_events_data, buckets_data, logs_data):
    '''
    Populate a test database to the sample structure
    '''

    from tests.unit import wrappers

    for bucket in buckets_data:
        wrappers.create_bucket(bucket)

    for fe in flow_events_data:
        wrappers.create_flow_event(fe)

    for log in logs_data:
        wrappers.create_log(log)
