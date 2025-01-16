from tests.client_fixtures import *
from tests.data_fixtures import *
from tests.unit import wrappers


def test_create_log(reset_db, logs_data):
    ''' Testing the success case of creating an log '''
    assert wrappers.create_log(logs_data[0])['status'] == SUCCESS


def test_get_all_log(reset_db, logs_data):
    ''' Testing the success case of getting all logs '''

    # Passes all log test data into database
    logs = [wrappers.create_log(logs_data[i])
            for i in range(0, len(logs_data))]

    # Checks all responses succeeds
    for log in logs:
        assert log["status"] == SUCCESS

    # Compare return list with input list
    all_logs = wrappers.get_all_logs()['data']
    # print("all_logs", all_logs)
    assert len(logs) == len(all_logs)


def test_get_log_by_log_id(reset_db, logs_data):
    ''' Testing the success case of getting specified log '''
    log = wrappers.create_log(logs_data[0])['data']
    ret_log = wrappers.get_log_by_log_id(log['id'])['data']
    assert log["name"] == ret_log["name"]


def test_invalid_get_log_by_log_id(reset_db, logs_data):
    ''' Testing the failing case of getting specified log '''
    log = wrappers.create_log(logs_data[0])['data']
    ret_log = wrappers.get_log_by_log_id(log['id'] + 200)
    assert ret_log['status'] == ERROR


def test_delete_log_by_log_id(reset_db, logs_data):
    ''' Testing the success case of deleting log '''
    log = wrappers.create_log(logs_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_log_by_log_id(log['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_log_by_log_id(log['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_log_by_log_id(log['id'])
    assert post_check_res['status'] == ERROR


def test_invalid_delete_log_by_log_id(reset_db, logs_data):
    ''' Testing the fail case of deleting log '''

    log = wrappers.create_log(logs_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_log_by_log_id(log['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_log_by_log_id(log['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_log_by_log_id(log['id'])
    assert post_check_res['status'] == SUCCESS


def test_update_log_by_log_id(reset_db, logs_data):
    ''' Testing the success case of updating log '''

    # Checks that created log and new log are different
    log = wrappers.create_log(logs_data[0])['data']
    new_log = logs_data[1]
    assert log['name'] != new_log['name']

    # Checks update response status is correct
    new_log = logs_data[1]
    update_log = wrappers.update_log_by_log_id(log['id'], new_log)
    assert update_log['status'] == SUCCESS

    # Check the update values are correct
    assert update_log['data']['name'] == new_log['name']


def test_invalid_update_log_by_log_id(reset_db, logs_data):
    ''' Testing the fail case of updating log '''

    # Checks update response status is invalid, from invalid ID provided
    log = wrappers.create_log(logs_data[0])['data']
    new_log = logs_data[1]
    update_log = wrappers.update_log_by_log_id(log['id'] + 200, new_log)
    assert update_log['status'] == ERROR

    # Checks that the current log is untouched
    curr_log = wrappers.get_log_by_log_id(log['id'])
    assert curr_log['data']['name'] == log['name']
