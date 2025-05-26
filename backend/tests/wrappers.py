from tests.fixtures.client import client, SUCCESS
import json



def unpack(function):
    ''' Wrapper to unpack the json values into parsable dictionary. Easier for testing '''
    def get_data(*args):
        resp = function(*args)
        if resp.status_code != SUCCESS:
            data = json.loads(resp.text)
            return {'status': resp.status_code,
                    'detail': data['detail']
                    }
        else:
            return {'status': resp.status_code,
                    'data': json.loads(resp.text)
                    }
    return get_data


# ====================== BUCKET WRAPPERS ======================

@unpack
def create_bucket(bucket_data):
    return client.post("/api/v1/bucket", json=bucket_data)

@unpack
def get_all_buckets():
    return client.get("/api/v1/buckets")

@unpack
def get_bucket_by_id(bucket_id):
    return client.get(f"/api/v1/bucket/{bucket_id}")

@unpack
def update_bucket_by_id(bucket_id, bucket_data):
    return client.patch(f"/api/v1/bucket/{bucket_id}", json=bucket_data)

@unpack
def delete_bucket_by_id(bucket_id):
    return client.delete(f"/api/v1/bucket/{bucket_id}")

# ====================== EVENT WRAPPERS ======================







@unpack
def create_event(event_data):
    return client.post("/api/v1/event", json=event_data)

@unpack
def get_all_events():
    return client.get("/api/v1/events")

@unpack
def get_event_by_id(event_id):
    return client.get(f"/api/v1/event/{event_id}")

@unpack
def update_event_by_id(event_id, event_data):
    return client.patch(f"/api/v1/event/{event_id}", json=event_data)

@unpack
def delete_event_by_id(event_id):
    return client.delete(f"/api/v1/event/{event_id}")


# ====================== LOG WRAPPERS ======================

@unpack
def create_log():
    pass

@unpack
def get_all_logs():
    pass

@unpack
def get_all_logs_by_bucket_id():
    pass

@unpack
def get_all_logs_by_time_range():
    pass

@unpack
def get_log_by_id():
    pass

@unpack
def delete_log_by_id():
    pass
