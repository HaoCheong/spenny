#!/usr/bin/python3

import requests
import sys
# Mainly so that I can use my phone as a method of triggering spenny

BUCKET_ID = 6

if __name__ == "__main__":

    amount_change = float(sys.argv[1])
    desc = sys.argv[2]
    
    body = {
        "name": "Daily Use",
        "description": f"Part of daily use: {desc}",
        "change_amount": amount_change,
        "type": "SUB",
        "from_bucket_id": BUCKET_ID,
    }
    res = requests.put('http://localhost:9101/soloTrigger', json=body)
