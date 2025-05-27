from tests.fixtures.client import SUCCESS, ERROR, reset_db
from tests.fixtures.data import event_data, bucket_data
from tests import wrappers


def test_create_event(reset_db, event_data, bucket_data):
    ''' Testing the success case of creating an event '''
    buckets = [wrappers.create_bucket(bucket_data[i])
               for i in range(0, len(bucket_data))]

    res = wrappers.create_event(event_data[0])

    assert res['status'] == SUCCESS


def test_get_all_event(reset_db, event_data, bucket_data):
    ''' Testing the success case of getting all events '''

    buckets = [wrappers.create_bucket(bucket_data[i])
               for i in range(0, len(bucket_data))]

    # Passes all event test data into database
    events = [wrappers.create_event(event_data[i])
              for i in range(0, len(event_data))]

    # Checks all responses succeeds
    for event in events:
        assert event["status"] == SUCCESS

    # Compare return list with input list
    all_events = wrappers.get_all_events()['data']['data']
    assert len(events) == len(all_events)


def test_get_event_by_id(reset_db, event_data, bucket_data):
    ''' Testing the success case of getting specified event '''

    buckets = [wrappers.create_bucket(bucket_data[i])
               for i in range(0, len(bucket_data))]

    event = wrappers.create_event(event_data[0])['data']
    ret_event = wrappers.get_event_by_id(event['id'])['data']

    # For every key value in event, ret event shares the same value
    for key, value in event.items():
        if ret_event[key] != value:
            assert False, f'Return value does not match with given value'

    assert True


def test_invalid_get_event_by_id(reset_db, event_data, bucket_data):
    ''' Testing the failing case of getting specified event '''

    buckets = [wrappers.create_bucket(bucket_data[i])
               for i in range(0, len(bucket_data))]

    event = wrappers.create_event(event_data[0])['data']
    ret_event = wrappers.get_event_by_id(event['id'] + 200)
    assert ret_event['status'] == ERROR, f'Invalid ID did not return error status on get by ID'


def test_delete_event_by_id(reset_db, event_data, bucket_data):
    ''' Testing the success case of deleting event '''

    buckets = [wrappers.create_bucket(bucket_data[i])
               for i in range(0, len(bucket_data))]

    event = wrappers.create_event(event_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_event_by_id(event['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_event_by_id(event['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_event_by_id(event['id'])
    assert post_check_res['status'] == ERROR, f'Deleted item\'s ID still present in database'


def test_invalid_delete_event_by_id(reset_db, event_data, bucket_data):
    ''' Testing the fail case of deleting event '''
    buckets = [wrappers.create_bucket(bucket_data[i])
               for i in range(0, len(bucket_data))]

    event = wrappers.create_event(event_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_event_by_id(event['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_event_by_id(event['id'] + 200)
    assert delete_res['status'] == ERROR, f'Invalid ID did not return error status on delete'

    # Check post-delete status
    post_check_res = wrappers.get_event_by_id(event['id'])
    assert post_check_res['status'] == SUCCESS


def test_update_event_by_id(reset_db, event_data, bucket_data):
    ''' Testing the success case of updating event '''

    buckets = [wrappers.create_bucket(bucket_data[i])
               for i in range(0, len(bucket_data))]

    # Checks that created event and new event are different
    event = wrappers.create_event(event_data[0])['data']
    new_event = event_data[1]
    assert event['name'] != new_event['name']
    assert event['description'] != new_event['description']
    assert event['trigger_datetime'] != new_event['trigger_datetime']
    assert event['frequency'] != new_event['frequency']
    assert event['event_type'] != new_event['event_type']

    # Checks update response status is correct
    new_event = event_data[1]
    update_event = wrappers.update_event_by_id(event['id'], new_event)
    assert update_event['status'] == SUCCESS

    # Check the update values are correct
    assert update_event['data']['name'] == new_event['name']
    assert update_event['data']['description'] == new_event['description']
    assert update_event['data']['trigger_datetime'] == new_event['trigger_datetime']
    assert update_event['data']['frequency'] == new_event['frequency']
    assert update_event['data']['event_type'] == new_event['event_type']


def test_invalid_update_event_by_id(reset_db, event_data, bucket_data):
    ''' Testing the fail case of updating event '''

    buckets = [wrappers.create_bucket(bucket_data[i])
               for i in range(0, len(bucket_data))]

    # Checks update response status is invalid, from invalid ID provided
    event = wrappers.create_event(event_data[0])['data']
    new_event = event_data[1]
    update_event = wrappers.update_event_by_id(
        event['id'] + 200, new_event)
    assert update_event['status'] == ERROR

    # Checks that the current event is untouched
    curr_event = wrappers.get_event_by_id(event['id'])
    assert curr_event['data']['name'] == event['name']
    assert curr_event['data']['description'] == event['description']
    assert curr_event['data']['trigger_datetime'] == event['trigger_datetime']
    assert curr_event['data']['frequency'] == event['frequency']
    assert curr_event['data']['event_type'] == event['event_type']
