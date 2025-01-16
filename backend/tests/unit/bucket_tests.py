<<<<<<< HEAD
from tests.data_fixtures import *
from tests.client_fixtures import *

from tests.unit import wrappers
=======
from tests.unit import wrappers
from tests.unit.client_fixtures import *
from tests.unit.data_fixtures import *
>>>>>>> master


def test_create_bucket(reset_db, buckets_data):
    ''' Testing the success case of creating an bucket '''
    assert wrappers.create_bucket(buckets_data[0])['status'] == SUCCESS


def test_get_all_bucket(reset_db, buckets_data):
    ''' Testing the success case of getting all buckets '''

    # Passes all bucket test data into database
    buckets = [wrappers.create_bucket(buckets_data[i])
               for i in range(0, len(buckets_data))]

    # Checks all responses succeeds
    for bucket in buckets:
        assert bucket["status"] == SUCCESS

    # Compare return list with input list
    all_buckets = wrappers.get_all_buckets()['data']
    # print("all_buckets", all_buckets)
    assert len(buckets) == len(all_buckets)


def test_get_bucket_by_bucket_id(reset_db, buckets_data):
    ''' Testing the success case of getting specified bucket '''
    bucket = wrappers.create_bucket(buckets_data[0])['data']
    ret_bucket = wrappers.get_bucket_by_bucket_id(bucket['id'])['data']
    assert bucket["name"] == ret_bucket["name"]


def test_invalid_get_bucket_by_bucket_id(reset_db, buckets_data):
    ''' Testing the failing case of getting specified bucket '''
    bucket = wrappers.create_bucket(buckets_data[0])['data']
    ret_bucket = wrappers.get_bucket_by_bucket_id(bucket['id'] + 200)
    assert ret_bucket['status'] == ERROR


def test_delete_bucket_by_bucket_id(reset_db, buckets_data):
    ''' Testing the success case of deleting bucket '''
    bucket = wrappers.create_bucket(buckets_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_bucket_by_bucket_id(bucket['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_bucket_by_bucket_id(bucket['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_bucket_by_bucket_id(bucket['id'])
    assert post_check_res['status'] == ERROR


def test_invalid_delete_bucket_by_bucket_id(reset_db, buckets_data):
    ''' Testing the fail case of deleting bucket '''

    bucket = wrappers.create_bucket(buckets_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_bucket_by_bucket_id(bucket['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_bucket_by_bucket_id(bucket['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_bucket_by_bucket_id(bucket['id'])
    assert post_check_res['status'] == SUCCESS


def test_update_bucket_by_bucket_id(reset_db, buckets_data):
    ''' Testing the success case of updating bucket '''

    # Checks that created bucket and new bucket are different
    bucket = wrappers.create_bucket(buckets_data[0])['data']
    new_bucket = buckets_data[1]
    assert bucket['name'] != new_bucket['name']

    # Checks update response status is correct
    new_bucket = buckets_data[1]
    update_bucket = wrappers.update_bucket_by_bucket_id(
        bucket['id'], new_bucket)
    assert update_bucket['status'] == SUCCESS

    # Check the update values are correct
    assert update_bucket['data']['name'] == new_bucket['name']


def test_invalid_update_bucket_by_bucket_id(reset_db, buckets_data):
    ''' Testing the fail case of updating bucket '''

    # Checks update response status is invalid, from invalid ID provided
    bucket = wrappers.create_bucket(buckets_data[0])['data']
    new_bucket = buckets_data[1]
    update_bucket = wrappers.update_bucket_by_bucket_id(
        bucket['id'] + 200, new_bucket)
    assert update_bucket['status'] == ERROR

    # Checks that the current bucket is untouched
    curr_bucket = wrappers.get_bucket_by_bucket_id(bucket['id'])
    assert curr_bucket['data']['name'] == bucket['name']
