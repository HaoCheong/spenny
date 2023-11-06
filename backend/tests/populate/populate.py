'''populate.py

Generates the sample database as per the example in docs
Acts as basic smoke testing for the APIs

'''

import requests
from datetime import datetime, timedelta
import random
  
BACKEND_URL = "http://127.0.0.1:8000"
  
def get_random_date():
	day_shift = random.randint(1, 7)
	today_date = datetime.now()
	new_date = today_date + timedelta(days=day_shift)
  
	return str(new_date)
  
  
all_buckets = [
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
  
all_flows = [
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
  
  
def add_all_buckets():
	for bkt in all_buckets:
		res = requests.post("{}/bucket".format(BACKEND_URL), json=bkt)
		if (res.status_code == 200):
			print(
				"ADDED BUCKET - {}, {}".format(bkt['name'], bkt['current_amount']))
  
  
def add_all_flowEvents():
	for fe in all_flows:
		res = requests.post("{}/flowEvent".format(BACKEND_URL), json=fe)
		if (res.status_code == 200):
			print(
				"ADDED FLOW EVENT - {}, {}, {}".format(fe['name'], fe['type'], fe['change_amount']))
  
  
if __name__ == "__main__":
	add_all_buckets()
	add_all_flowEvents()