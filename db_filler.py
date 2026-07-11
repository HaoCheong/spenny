#!/usr/bin/python3

import requests

BACKEND_URL = "http://192.168.30.238:8682"

BUCKETS = [
    {
        "name": "Bucket A for Storing",
        "description": "Bucket A for Andrew for storing",
        "amount": 500000,
        "variant": {
            "type": "STORE"
        }
    },
    {
        "name": "Bucket B is invisible",
        "description": "Bucket b for Bandrew but invisble",
        "amount": 200000,
        "variant": {
            "type": "INVSB"
        }
    },
    {
        "name": "Bucket C is Goals",
        "description": "Bucket c for Candrew for Goals",
        "amount": 100000,
        "variant": {
            "type": "GOALS",
            "target": 500000
        }
    }
]

EVENTS = [
    {
        "name": "A to B",
        "description": "Moving Money from A to B",
        "bucket_id": 1,
        "trigger": {
            "type": "timed",
            "frequency": "3m",
            "next_trigger_date": "2025-03-15T10:24:42.687Z"
        },
        "operation": {
            "to_bucket_id": 2,
            "type": "MOVE",
            "amount": 12300
        }
    },
    {
        "name": "Add Money to A",
        "description": "Adding Money to A",
        "bucket_id": 1,
        "trigger": {
            "type": "timed",
            "frequency": "1m",
            "next_trigger_date": "2025-04-20T10:24:42.687Z"
        },
        "operation": {
            "type": "ADD",
            "amount": 55500
        }
    },
    {
        "name": "Subtract Money from B",
        "description": "Subtracting Money from B",
        "bucket_id": 2,
        "trigger": {
            "type": "timed",
            "frequency": "2m",
            "next_trigger_date": "2025-05-25T10:24:42.687Z"
        },
        "operation": {
            "type": "SUB",
            "amount": 11100
        }
    },
    {
        "name": "Add Money to C",
        "description": "Adding Money from C",
        "bucket_id": 2,
        "trigger": {
            "type": "timed",
            "frequency": "10m",
            "next_trigger_date": "2025-01-10T10:24:42.687Z"
        },
        "operation": {
            "type": "ADD",
            "amount": 22200
        }
    }
] 

def post_event(event):
    print(f"ADDING EVENT: {event}")
    try:
        requests.post(f"{BACKEND_URL}/api/v1/event", json=event)
    except Exception as e:
        (f"ERROR for Event: {event} - Error: {e}")
    

def post_bucket(bucket):
    print(f"ADDING BUCKET: {bucket}")
    try:
        requests.post(f"{BACKEND_URL}/api/v1/bucket", json=bucket)
    except Exception as e:
        print(f"ERROR for bucket: {bucket} - Error: {e}")
    

if __name__ == "__main__":
    
    for bucket in BUCKETS:
        post_bucket(bucket)

    for event in EVENTS:
        post_event(event)
