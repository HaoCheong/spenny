from tests.unit import wrappers
from tests.unit.client_fixtures import *
from tests.unit.client_fixtures import ERROR, SUCCESS
from tests.unit.data_fixtures import *


def test_create_flow_event(reset_db, flow_events_data):
    ''' Testing the success case of creating an flow_event '''
    assert wrappers.create_flow_event(flow_events_data[0])['status'] == SUCCESS


def test_get_all_flow_event(reset_db, flow_events_data):
    ''' Testing the success case of getting all flow_events '''

    # Passes all flow_event test data into database
    flow_events = [wrappers.create_flow_event(flow_events_data[i])
                   for i in range(0, len(flow_events_data))]

    # Checks all responses succeeds
    for flow_event in flow_events:
        assert flow_event["status"] == SUCCESS

    # Compare return list with input list
    all_flow_events = wrappers.get_all_flow_events()['data']
    # print("all_flow_events", all_flow_events)
    assert len(flow_events) == len(all_flow_events)


def test_get_flow_event_by_flow_event_id(reset_db, flow_events_data):
    ''' Testing the success case of getting specified flow_event '''
    flow_event = wrappers.create_flow_event(flow_events_data[0])['data']
    ret_flow_event = wrappers.get_flow_event_by_flow_event_id(flow_event['id'])[
        'data']
    assert flow_event["name"] == ret_flow_event["name"]


def test_invalid_get_flow_event_by_flow_event_id(reset_db, flow_events_data):
    ''' Testing the failing case of getting specified flow_event '''
    flow_event = wrappers.create_flow_event(flow_events_data[0])['data']
    ret_flow_event = wrappers.get_flow_event_by_flow_event_id(
        flow_event['id'] + 200)
    assert ret_flow_event['status'] == ERROR


def test_delete_flow_event_by_flow_event_id(reset_db, flow_events_data):
    ''' Testing the success case of deleting flow_event '''
    flow_event = wrappers.create_flow_event(flow_events_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_flow_event_by_flow_event_id(flow_event['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status
    delete_res = wrappers.delete_flow_event_by_flow_event_id(flow_event['id'])
    assert delete_res['status'] == SUCCESS

    # Check post-delete status
    post_check_res = wrappers.get_flow_event_by_flow_event_id(flow_event['id'])
    assert post_check_res['status'] == ERROR

def test_invalid_delete_flow_event_by_flow_event_id(reset_db, flow_events_data):
    ''' Testing the fail case of deleting flow_event '''

    flow_event = wrappers.create_flow_event(flow_events_data[0])['data']

    # Check pre-delete status
    pre_check_res = wrappers.get_flow_event_by_flow_event_id(flow_event['id'])
    assert pre_check_res['status'] == SUCCESS

    # Check deletion request status, with invalid ID provided
    delete_res = wrappers.delete_flow_event_by_flow_event_id(
        flow_event['id'] + 200)
    assert delete_res['status'] == ERROR

    # Check post-delete status
    post_check_res = wrappers.get_flow_event_by_flow_event_id(flow_event['id'])
    assert post_check_res['status'] == SUCCESS

def test_update_flow_event_by_flow_event_id(reset_db, flow_events_data):
    ''' Testing the success case of updating flow_event '''

    # Checks that created flow_event and new flow_event are different
    flow_event = wrappers.create_flow_event(flow_events_data[0])['data']
    new_flow_event = flow_events_data[1]
    assert flow_event['name'] != new_flow_event['name']

    # Checks update response status is correct
    new_flow_event = flow_events_data[1]
    update_flow_event = wrappers.update_flow_event_by_flow_event_id(
        flow_event['id'], new_flow_event)
    assert update_flow_event['status'] == SUCCESS

    # Check the update values are correct
    assert update_flow_event['data']['name'] == new_flow_event['name']

def test_invalid_update_flow_event_by_flow_event_id(reset_db, flow_events_data):
    ''' Testing the fail case of updating flow_event '''

    # Checks update response status is invalid, from invalid ID provided
    flow_event = wrappers.create_flow_event(flow_events_data[0])['data']
    new_flow_event = flow_events_data[1]
    update_flow_event = wrappers.update_flow_event_by_flow_event_id(
        flow_event['id'] + 200, new_flow_event)
    assert update_flow_event['status'] == ERROR

    # Checks that the current flow_event is untouched
    curr_flow_event = wrappers.get_flow_event_by_flow_event_id(
        flow_event['id'])
    assert curr_flow_event['data']['name'] == flow_event['name']
