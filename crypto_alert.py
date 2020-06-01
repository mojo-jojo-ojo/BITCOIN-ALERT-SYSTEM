import json
import requests
import time
from boltiot import Bolt



SELLING_PRICE  =0  #for checking if the system works, you can input the selling price as per your choice

API_KEY = ""   # Enter the API key of your bolt product
DEVICE_ID  = ""                              #device id of the  bolt device, Eg: BOLTXXXX where XXXX are the number
bolt = Bolt(API_KEY, DEVICE_ID)


def price_check():
    url = "https://min-api.cryptocompare.com/data/price"

    querystring = {"fsym":"BTC","tsyms":"INR"}

    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)
    current_price = response['INR']
    return current_price

while True:
    time.sleep(10)
    market_price = price_check()
    print("Market price is", market_price," INR")
    print("Selling price is", SELLING_PRICE," INR")

    if market_price > SELLING_PRICE:
        bolt.digitalWrite("0","HIGH")
        time.sleep(0.2)
        bolt.digitalWrite("0","LOW")
        time.sleep(0.2)
        bolt.digitalWrite("0","HIGH")
        time.sleep(0.2)
        bolt.digitalWrite("0", "LOW")




