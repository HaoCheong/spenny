from tests.fixtures.client import SUCCESS, ERROR, reset_db
from tests.fixtures.data import bucket_data
from tests import wrappers


def test_create_bucket(reset_db, bucket_data):
    ''' Testing the success case of creating an bucket '''

    res = wrappers.create_bucket(bucket_data[0])
    assert res['status'] == SUCCESS


def test_get_all_bucket(reset_db, bucket_data):
    ''' Testing the success case of getting all buckets '''

    # Passes all bucket test data into database
    buckets = [wrappers.create_bucket(bucket_data[i])
              for i in range(0, len(bucket_data))]
    
    # Checks all responses succeeds
    for bucket in buckets:
        assert bucket["status"] == SUCCESS

    # Compare return list with input list
    all_buckets = wrappers.get_all_buckets()['data']['data']
    assert len(buckets) == len(all_buckets)


def test_get_bucket_by_id(reset_db, bucket_data):
    ''' Testing the success case of getting specified bucket '''
    bucket = wrappers.create_bucket(bucket_data[0])['data']
    ret_bucket = wrappers.get_bucket_by_id(bucket['id'])['data']

    # For every key value in bucket, ret bucket shares the same value
    for key, value in bucket.items():
        if ret_bucket[key] != value:
            assert False, f'Return value does not match with given value'

    assert True


def test_invalid_get_bucket_by_id(reset_db, bucket_data):
    ''' Testing the failing case of getting specified bucket '''
    bucket = wrappers.create_bucket(bucket_data[0])['data']
    ret_bucket = wrappers.get_bucket_by_id(bucket['id'] + 200)
    assert ret_bucket['status'] == ERROR, f'Invalid ID did not return error status on get by ID'


def test_delete_bucket_by_id(reset_db, bucket_data):
    ''' Testing the success case of deleting bucket '''
    bucket = wrappers.create_bucket(bucket_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_bucket_by_id(bucket['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_bucket_by_id(bucket['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_bucket_by_id(bucket['id'])
    assert post_check_res['status'] == ERROR, f'Deleted item\'s ID still present in database'


def test_invalid_delete_bucket_by_id(reset_db, bucket_data):
    ''' Testing the fail case of deleting bucket '''

    bucket = wrappers.create_bucket(bucket_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_bucket_by_id(bucket['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_bucket_by_id(bucket['id'] + 200)
    assert delete_res['status'] == ERROR, f'Invalid ID did not return error status on delete'

    # Check post-delete status
    post_check_res = wrappers.get_bucket_by_id(bucket['id'])
    assert post_check_res['status'] == SUCCESS


def test_update_bucket_by_id(reset_db, bucket_data):
    ''' Testing the success case of updating bucket '''

    # Checks that created bucket and new bucket are different
    bucket = wrappers.create_bucket(bucket_data[0])['data']
    new_bucket = bucket_data[1]
    assert bucket['name'] != new_bucket['name']
    assert bucket['description'] != new_bucket['description']
    assert bucket['amount'] != new_bucket['amount']

    # Checks update response status is correct
    new_bucket = bucket_data[1]
    update_bucket = wrappers.update_bucket_by_id(bucket['id'], new_bucket)
    assert update_bucket['status'] == SUCCESS

    # Check the update values are correct
    assert update_bucket['data']['name'] == new_bucket['name']
    assert update_bucket['data']['description'] == new_bucket['description']
    assert update_bucket['data']['amount'] == new_bucket['amount']
    assert update_bucket['data']['bucket_type'] == new_bucket['bucket_type']


def test_invalid_update_bucket_by_id(reset_db, bucket_data):
    ''' Testing the fail case of updating bucket '''

    # Checks update response status is invalid, from invalid ID provided
    bucket = wrappers.create_bucket(bucket_data[0])['data']
    new_bucket = bucket_data[1]
    update_bucket = wrappers.update_bucket_by_id(
        bucket['id'] + 200, new_bucket)
    assert update_bucket['status'] == ERROR

    # Checks that the current bucket is untouched
    curr_bucket = wrappers.get_bucket_by_id(bucket['id'])
    assert curr_bucket['data']['name'] == bucket['name']
    assert curr_bucket['data']['description'] == bucket['description']
    assert curr_bucket['data']['amount'] == bucket['amount']
    assert curr_bucket['data']['bucket_type'] == bucket['bucket_type']
