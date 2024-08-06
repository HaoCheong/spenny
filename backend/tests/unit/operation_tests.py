from tests.unit.data_fixtures import *

from tests.unit import wrappers

# ========== Bucket Operations Tests ==========


def test_update_bucket_values():
    pass


def test_update_all_buckets():
    pass


# ========== Trigger Operations Tests ==========


def test_manual_trigger():
    pass


def test_bring_forward():
    pass

# ========== Operations Helper Tests ==========


def test_change_bucket_value():
    pass

# ========== OTHER ==========


def test_other(populate_database):
    db_buckets = wrappers.get_all_buckets()
    print("DB_BUCKET", db_buckets)
    pass
