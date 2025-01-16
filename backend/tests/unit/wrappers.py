import json

from tests.client_fixtures import ERROR, SUCCESS, client, reset_db
from tests.data_fixtures import *


def unpack(function):
    """ Wrapper to unpack the json values into parsable dictionary. Easier for testing """
    def get_data(*args):
        resp = function(*args)
        if resp.status_code != SUCCESS:
            data = json.loads(resp.text)
            return {"status": resp.status_code,
                    "detail": data["detail"]
                    }
        else:
            return {"status": resp.status_code,
                    "data": json.loads(resp.text)
                    }
    return get_data

# ======== BUCKET WRAPPERS ========


@unpack
def create_bucket(bucket_data):
    """ Wrapper to emulate creating an bucket """
    return client.post("/api/v1/bucket", json=bucket_data)


@unpack
def get_all_buckets():
    """ Wrapper to emulate getting all buckets """
    return client.get("/api/v1/buckets")


@unpack
def get_bucket_by_bucket_id(bucket_id):
    """ Wrapper to emulate getting specified bucket """
    return client.get(f"/api/v1/bucket/{bucket_id}")


@unpack
def delete_bucket_by_bucket_id(bucket_id):
    """ Wrapper to emulate deleting specified bucket """
    return client.delete(f"/api/v1/bucket/{bucket_id}")


@unpack
def update_bucket_by_bucket_id(bucket_id, bucket_dict):
    """ Wrapper to emulate updating specified bucket """
    return client.patch(f"/api/v1/bucket/{bucket_id}", json=bucket_dict)

# ======== FLOW EVENT WRAPPERS ========


@unpack
def create_flow_event(flow_event_data):
    """ Wrapper to emulate creating an flow_event """
    return client.post("/api/v1/flowEvent", json=flow_event_data)


@unpack
def get_all_flow_events():
    """ Wrapper to emulate getting all flow_events """
    return client.get("/api/v1/flowEvents")


@unpack
def get_flow_event_by_flow_event_id(flow_event_id):
    """ Wrapper to emulate getting specified flow_event """
    return client.get(f"/api/v1/flowEvent/{flow_event_id}")


@unpack
def delete_flow_event_by_flow_event_id(flow_event_id):
    """ Wrapper to emulate deleting specified flow_event """
    return client.delete(f"/api/v1/flowEvent/{flow_event_id}")


@unpack
def update_flow_event_by_flow_event_id(flow_event_id, flow_event_dict):
    """ Wrapper to emulate updating specified flow_event """
    return client.patch(f"/api/v1/flowEvent/{flow_event_id}", json=flow_event_dict)

# ======== LOG WRAPPERS ========


@unpack
def create_log(log_data):
    """ Wrapper to emulate creating an log """
    return client.post("/api/v1/log", json=log_data)


@unpack
def get_all_logs():
    """ Wrapper to emulate getting all logs """
    return client.get("/api/v1/logs")


@unpack
def get_log_by_log_id(log_id):
    """ Wrapper to emulate getting specified log """
    return client.get(f"/api/v1/log/{log_id}")


@unpack
def delete_log_by_log_id(log_id):
    """ Wrapper to emulate deleting specified log """
    return client.delete(f"/api/v1/log/{log_id}")


@unpack
def update_log_by_log_id(log_id, log_dict):
    """ Wrapper to emulate updating specified log """
    return client.patch(f"/api/v1/log/{log_id}", json=log_dict)

# ======== OPERATION WRAPPERS ========


@unpack
def update_all_buckets():
    return client.put('/api/v1/updateValues')
