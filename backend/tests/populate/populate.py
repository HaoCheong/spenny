'''populate.py

Generates the sample database as per the example in docs
Acts as basic smoke testing for the APIs

'''

import requests
from datetime import datetime, timedelta
import random

BACKEND_URL = "http://127.0.0.1:9991"

def get_random_date():
	day_shift = random.randint(1, 7)
	today_date = datetime.now()
	new_date = today_date + timedelta(days=day_shift)
  
	return str(new_date)

ALL_BUCKETS = [
	{
		"name": "Total",
		"description": "Total amount in account",
		"current_amount": 10000.0,
		"properties": {
			"invisible": False
		}
	},
	{
		"name": "Savings",
		"description": "General Savings",
		"current_amount": 1800.0,
		"properties": {
			"invisible": False
		}
	},
	{
		"name": "Lifestyle",
		"description": "Everything from food to fun",
		"current_amount": 200.0,
		"properties": {
			"invisible": False
		}
	},
	{
		"name": "Food",
		"description": "My crippling eating habits",
		"current_amount": 0.0,
		"properties": {
			"invisible": False
		}
	},
	{
		"name": "Fun",
		"description": "For my hobbies and fun stuff ",
		"current_amount": 0.0,
		"properties": {
			"invisible": False
		}
	},
  
]
  
ALL_FLOWS = [
	{
		"name": "Main Job income",
		"description": "My main salary",
		"change_amount": 5562.0,
		"type": "ADD",
		"frequency": "5d",
		"from_bucket_id": None,
		"to_bucket_id": 1,
		"next_trigger": get_random_date()
	},
	{
		"name": "Savings",
		"description": "Automated saving move",
		"change_amount": 1800.0,
		"type": "MOV",
		"frequency": "3d",
		"from_bucket_id": 1,
		"to_bucket_id": 2,
		"next_trigger": get_random_date()
	},
	{
		"name": "Rent",
		"description": "Purely to live at my apartment",
		"change_amount": 560.0,
		"type": "SUB",
		"frequency": "5d",
		"from_bucket_id": 1,
		"to_bucket_id": None,
		"next_trigger": get_random_date()
	},
	{
		"name": "Gym",
		"description": "Fitness Finance",
		"change_amount": 18.0,
		"type": "SUB",
		"frequency": "2d",
		"from_bucket_id": 1,
		"to_bucket_id": None,
		"next_trigger": get_random_date()
	},
	{
		"name": "Lifestyle",
		"description": "Money for actually living in the cruel world",
		"change_amount": 240.0,
		"type": "MOV",
		"frequency": "4d",
		"from_bucket_id": 1,
		"to_bucket_id": 3,
		"next_trigger": get_random_date()
	},
	{
		"name": "Food",
		"description": "Budget for eating",
		"change_amount": 200.0,
		"type": "MOV",
		"frequency": "3d",
		"from_bucket_id": 3,
		"to_bucket_id": 4,
		"next_trigger": get_random_date()
	},
	{
		"name": "Fun",
		"description": "Hobby Funding",
		"change_amount": 40.0,
		"type": "MOV",
		"frequency": "1d",
		"from_bucket_id": 3,
		"to_bucket_id": 5,
		"next_trigger": get_random_date()
	},
]

ALL_LOGS = [
        {
            "name": "Main Job income",
            "description": "My main salary",
            "type": "ADD",
            "amount": 5000,
            "date_created": get_random_date(),
            "bucket_id": 1
        },
        {
            "name": "Gym Spending",
            "description": "For exercise",
            "type": "SUB",
            "amount": 18,
            "date_created": get_random_date(),
            "bucket_id": 1
        },
        {
            "name": "Household spending move",
            "description": "Moving Total to household spending",
            "type": "MOV",
            "amount": 600,
            "date_created": get_random_date(),
            "bucket_id": 1
        },
        {
            "name": "Savings Move",
            "description": "Money to be saved on untouched",
            "type": "MOV",
            "amount": 2000,
            "date_created": get_random_date(),
            "bucket_id": 1
        },
        {
            "name": "Woolies shopping",
            "description": "Friday woolies shopping",
            "type": "SUB",
            "amount": 65,
            "date_created": get_random_date(),
            "bucket_id": 5
        },
        {
            "name": "Eating at Cafe de la Cafe",
            "description": "Brekkie",
            "type": "SUB",
            "amount": 30,
            "date_created": get_random_date(),
            "bucket_id": 5
        },
        {
            "name": "Bought Video Game 2: More games",
            "description": "Let me be happy",
            "type": "SUB",
            "amount": 55,
            "date_created": get_random_date(),
            "bucket_id": 6
        }
    ]


def populate_buckets():
	''' Populates database with bucket data '''
	print("========== ADDING BUCKETS ==========")
	for bkt in ALL_BUCKETS:
		try:
			res = requests.post(f"{BACKEND_URL}/bucket", json=bkt)
			if res.status_code != 200:
				raise ValueError
			
			print("Added BUCKET - %s" % bkt)
		except ValueError:
			print("Failed to add BUCKET - %s" % bkt)


def populate_flow_events():
	''' Populates database with flow event data '''
	print("========== ADDING FLOW EVENT ==========")
	for fe in ALL_FLOWS:
		try:
			res = requests.post(f"{BACKEND_URL}/flowEvent", json=fe)
			if res.status_code != 200:
				raise ValueError
			
			print("Added FLOW EVENT - %s" % fe)
		except ValueError:
			print("Failed to add FLOW EVENT - %s" % fe)


def populate_logs():
	''' Populates database with log data '''
	print("========== ADDING LOG ==========")
	for fe in ALL_LOGS:
		try:
			res = requests.post(f"{BACKEND_URL}/log", json=fe)
			if res.status_code != 200:
				raise ValueError
			
			print("Added LOG - %s" % fe)
		except ValueError:
			print("Failed to add LOG - %s" % fe)
  
  
if __name__ == "__main__":
	populate_buckets()
	populate_flow_events()
	populate_logs()
