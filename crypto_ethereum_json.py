'''
This program queries coingecko for ethereum prices in USD
It only runs for one coin, ethereum
The urls require a specific date, and are generated using the datetime timedelta library, to handle things like leap year(s)
The data is written to a csv
'''


import requests
import json
import time
import os
from datetime import datetime, timedelta


# example url for coingecko.com
example_url = "https://api.coingecko.com/api/v3/coins/ethereum/history?date=23-09-2024&localization=false"

response = requests.get(example_url)
dictionary = response.json()

market_data_key = "market_data"
current_price_key= "current_price"
usd_key = "usd"

usd = dictionary[market_data_key][current_price_key][usd_key]
print(usd)