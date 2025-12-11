from tests.fixtures.client import SUCCESS, ERROR, reset_db
from tests.fixtures.data import log_data
from tests import wrappers

from datetime import datetime


def test_create_log(reset_db, log_data):
    ''' Testing the success case of creating an log '''

    res = wrappers.create_log(log_data[0])
    assert res['status'] == SUCCESS


def test_get_all_log(reset_db, log_data):
    ''' Testing the success case of getting all logs '''

    # Passes all log test data into database
    logs = [wrappers.create_log(log_data[i])
            for i in range(0, len(log_data))]

    # Checks all responses succeeds
    for log in logs:
        assert log["status"] == SUCCESS

    # Compare return list with input list
    all_logs = wrappers.get_all_logs()['data']['data']
    assert len(logs) == len(all_logs)


def test_get_log_by_id(reset_db, log_data):
    ''' Testing the success case of getting specified log '''
    log = wrappers.create_log(log_data[0])['data']
    ret_log = wrappers.get_log_by_id(log['id'])['data']

    # For every key value in log, ret log shares the same value
    for key, value in log.items():
        if ret_log[key] != value:
            assert False, f'Return value does not match with given value'

    assert True


def test_invalid_get_log_by_id(reset_db, log_data):
    ''' Testing the failing case of getting specified log '''
    log = wrappers.create_log(log_data[0])['data']
    ret_log = wrappers.get_log_by_id(log['id'] + 200)
    assert ret_log['status'] == ERROR, f'Invalid ID did not return error status on get by ID'


def test_delete_log_by_id(reset_db, log_data):
    ''' Testing the success case of deleting log '''
    log = wrappers.create_log(log_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_log_by_id(log['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_log_by_id(log['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_log_by_id(log['id'])
    assert post_check_res['status'] == ERROR, f'Deleted item\'s ID still present in database'


def test_invalid_delete_log_by_id(reset_db, log_data):
    ''' Testing the fail case of deleting log '''

    log = wrappers.create_log(log_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_log_by_id(log['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_log_by_id(log['id'] + 200)
    assert delete_res['status'] == ERROR, f'Invalid ID did not return error status on delete'

    # Check post-delete status
    post_check_res = wrappers.get_log_by_id(log['id'])
    assert post_check_res['status'] == SUCCESS


def test_valid_get_all_logs_by_bucket_id(reset_db):

    test_bucket_id = 1

    res = wrappers.get_all_logs_by_bucket_id(test_bucket_id)
    data = res.get("data")
    assert res.get("status") == SUCCESS

    assert data.get("total") == len(data.get("data"))

    for log in data.get("data"):
        assert log['bucket_id'] == test_bucket_id
