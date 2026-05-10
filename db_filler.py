#!/usr/bin/python3

import requests

BACKEND_URL = "http://192.168.30.238:8682"

BUCKETS = [
    {
        "name": "Bucket A for Storing",
        "description": "Bucket A for Andrew for storing",
        "amount": 5000,
        "variant": {
            "type": "STORE"
        }
    },
    {
        "name": "Bucket B is invisible",
        "description": "Bucket b for Bandrew but invisble",
        "amount": 2000,
        "variant": {
            "type": "INVSB"
        }
    },
    {
        "name": "Bucket C is Goals",
        "description": "Bucket c for Candrew for Goals",
        "amount": 1000,
        "variant": {
            "type": "GOALS",
            "target": 5000
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
            "frequency": "1m",
            "next_trigger_date": "2026-03-15T10:24:42.687Z"
        },
        "operation": {
            "to_bucket_id": 2,
            "type": "MOVE",
            "amount": 100
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
