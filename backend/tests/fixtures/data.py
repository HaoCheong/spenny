
import pytest

@pytest.fixture
def bucket_data():
    ''' Return test bucket data '''
    return [
        {
            "name": "Bills",
            "description": "Utility Bills and Spending",
            "amount": 0,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Health Insurance",
            "description": "Medical Health Insurance",
            "amount": 450,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Weekly Spending",
            "description": "Grocery and Eating out spending",
            "amount": 2400,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Household",
            "description": "Household Expenses",
            "amount": -4400,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Start",
            "description": "Starting Bucket",
            "amount": 5000,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Rent",
            "description": "Rent cost and portioning",
            "amount": 600,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Gym",
            "description": "Spending at the Gym",
            "amount": 780,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Debt",
            "description": "Debts I owe people",
            "amount": 6000,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Savings",
            "description": "Savings that are accumulated",
            "amount": 5070,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Lifestyle",
            "description": "Lifestyle personal uses",
            "amount": 0,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Fun Fund",
            "description": "Spending for wants",
            "amount": 600,
            "bucket_type": "STORE",
            "properties": None,
        },
        {
            "name": "Necessity",
            "description": "Necessary Spending",
            "amount": -450,
            "bucket_type": "STORE",
            "properties": None,
    
        }
    ]

@pytest.fixture
def event_data():
    ''' Return test event data '''
    return [
        {
            "name": "Savings Transfer",
            "description": "Monthly Transfer for to savings account",
            "trigger_datetime": "2025-06-02T11:28:02.028000",
            "frequency": "1m",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 5,
                "amount": 1690
            },
            "bucket_id": 1,
        },
        {
            "name": "Lifestyle Transfer",
            "description": "Monthly Transfer for lifestyle",
            "trigger_datetime": "2025-06-02T11:28:02.028000",
            "frequency": "1m",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 4,
                "amount": 1260
            },
            "bucket_id": 1,
        },
        {
            "name": "Auto Rental Payment",
            "description": "Fortnightly rental payment",
            "trigger_datetime": "2025-05-23T11:28:02.028000",
            "frequency": "2w",
            "event_type": "SUB",
            "properties": {
                "amount": 1000
            },
            "bucket_id": 2,
        },
        {
            "name": "Weekly Spending Transfer",
            "description": "Weekly Transfer for Groceries and what not",
            "trigger_datetime": "2025-05-26T11:28:02.028000",
            "frequency": "1w",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 11,
                "amount": 200
            },
            "bucket_id": 4,
        },
        {
            "name": "Health Insurance Payment",
            "description": "Monthly Medicare payment",
            "trigger_datetime": "2025-06-07T11:28:02.028000",
            "frequency": "1m",
            "event_type": "SUB",
            "properties": {
                "amount": 150
            },
            "bucket_id": 3,
        },
        {
            "name": "Necessity Transfer",
            "description": "Monthly Transfer for necessity",
            "trigger_datetime": "2025-06-02T11:28:02.028000",
            "frequency": "1m",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 3,
                "amount": 150
            },
            "bucket_id": 1,
        },
        {
            "name": "Household Transfer",
            "description": "Monthly Transfer of household stuff",
            "trigger_datetime": "2025-06-02T11:28:02.028000",
            "frequency": "1m",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 2,
                "amount": 2400
            },
            "bucket_id": 1,
        },
        {
            "name": "PT Transfer",
            "description": "Weekly Transfer for Personal Trainer",
            "trigger_datetime": "2025-05-26T11:28:02.028000",
            "frequency": "2w",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 12,
                "amount": 100
            },
            "bucket_id": 4,
        },
        {
            "name": "Salary",
            "description": "Monthly Salary, paid on the last working day of the month",
            "trigger_datetime": "2027-10-01T11:26:42.614000",
            "frequency": "1m",
            "event_type": "ADD",
            "properties": {
                "amount": 5500
            },
            "bucket_id": 1,
        },
        {
            "name": "Fun Fund Transfer",
            "description": "Weekly Transfer for fun stuff fund",
            "trigger_datetime": "2025-05-26T11:28:02.028000",
            "frequency": "1w",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 10,
                "amount": 50
            },
            "bucket_id": 4,
        },
        {
            "name": "Health Insurance Transfer",
            "description": "Monthly Transfer for medicare health insurance",
            "trigger_datetime": "2025-06-03T11:28:02.028000",
            "frequency": "1m",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 9,
                "amount": 150
            },
            "bucket_id": 3,
        },
        {
            "name": "Gym Transfer",
            "description": "Weekly Transfer for gym membership",
            "trigger_datetime": "2025-05-26T11:28:02.028000",
            "frequency": "1w",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 12,
                "amount": 15
            },
            "bucket_id": 4,
        },
        {
            "name": "Bill Transfer",
            "description": "Monthly Transfer for utilities: Gas, Electric, Internet",
            "trigger_datetime": "2025-06-03T11:28:02.028000",
            "frequency": "1m",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 7,
                "amount": 200
            },
            "bucket_id": 2,
        },
        {
            "name": "Rent Transfer",
            "description": "Monthly Transfer for rent",
            "trigger_datetime": "2025-06-03T11:28:02.028000",
            "frequency": "1m",
            "event_type": "MOVE",
            "properties": {
                "to_bucket_id": 6,
                "amount": 2000
            },
            "bucket_id": 2,
        }
    ]

@pytest.fixture
def log_data():
    return [
        {
            "name": "Auto Rental Payment",
            "description": "Fortnightly rental payment",
            "log_type": "EVENT",
            "event_id": 13,
            "event_type": "SUB",
            "event_properties": {
                "amount": 1000
            },
            "bucket_id": 2,
            "bucket_name": "Household",
        },
        {
            "name": "Auto Rental Payment",
            "description": "Fortnightly rental payment",
            "log_type": "EVENT",
            "event_id": 13,
            "event_type": "SUB",
            "event_properties": {
                "amount": 1000
            },
            "bucket_id": 2,
            "bucket_name": "Household",
        },
        {
            "name": "Auto Rental Payment",
            "description": "Fortnightly rental payment",
            "log_type": "EVENT",
            "event_id": 13,
            "event_type": "SUB",
            "event_properties": {
                "amount": 1000
            },
            "bucket_id": 2,
            "bucket_name": "Household",
        }
    ]