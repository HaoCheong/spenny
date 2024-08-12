from tests.unit.data_fixtures import *
from tests.unit import wrappers
from tests.unit.client_fixtures import get_test_db
import app.operations.operation_helpers as oph
from fastapi.encoders import jsonable_encoder

# ========== Bucket Operations Tests ==========


def test_update_bucket_values(populate_database):
    pass


def test_update_all_buckets(populate_database):
    pass


# ========== Trigger Operations Tests ==========


def test_manual_trigger(populate_database):
    pass


def test_bring_forward(populate_database):
    pass

# ========== Operations Helper Tests ==========


def test_change_bucket_value(populate_database):

    test_db = get_test_db()
    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))['data']
    print(test_bucket)
    test_curr_amount = test_bucket['current_amount']
    test_amount = 100
    print("PRE", test_bucket)

    oph.change_bucket_value(test_bucket, 'ADD', test_amount, test_db)

    test_bucket = jsonable_encoder(wrappers.get_bucket_by_bucket_id(1))
    print("POST", test_bucket)
    pass

# ========== OTHER ==========


def test_other(populate_database, get_test_db):

    test_db = get_test_db
    db_buckets = wrappers.get_all_buckets()

    print("DB_BUCKET", db_buckets)
    print("TEST_DB", type(test_db))
    pass
