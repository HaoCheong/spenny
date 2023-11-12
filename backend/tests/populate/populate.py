'''populate.py

Generates the sample database as per the example in docs
Acts as basic smoke testing for the APIs

'''

import requests
from datetime import datetime, timedelta
import random
<<<<<<< HEAD
  
BACKEND_URL = "http://127.0.0.1:8000"
  
=======

BACKEND_URL = "http://127.0.0.1:8000"

>>>>>>> f6c987c5d47295c32301375147826999d79cb416
def get_random_date():
	day_shift = random.randint(1, 7)
	today_date = datetime.now()
	new_date = today_date + timedelta(days=day_shift)
  
	return str(new_date)

ALL_BUCKETS = [
	{
		"name": "Total",
		"description": "Total amount in account",
		"current_amount": 10000.0
	},
	{
		"name": "Savings",
		"description": "General Savings",
		"current_amount": 1800.0
	},
	{
		"name": "Lifestyle",
		"description": "Everything from food to fun",
		"current_amount": 200.0
	},
	{
		"name": "Food",
		"description": "My crippling eating habits",
		"current_amount": 0.0
	},
	{
		"name": "Fun",
		"description": "For my hobbies and fun stuff ",
		"current_amount": 0.0
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


def populate_flow_event():
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
  
  
if __name__ == "__main__":
	populate_buckets()
	populate_flow_event()