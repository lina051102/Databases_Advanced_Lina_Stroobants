import requests
from time import sleep
from bs4 import BeautifulSoup
import pymongo as mongo
import redis

# MongoDB
## Connecting to database
client = mongo.MongoClient("mongodb://127.0.0.1:27017")

## Make new database
my_bit_database = client["Scraper"]

## Setting column
col_bitcoin = my_bit_database["BitcoinData"]

# Redis
red = redis.StrictRedis(host='localhost', port=6380, db=0)

while True:
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text,features="html5lib")

    if soup.find("div", class_="sc-1g6z4xm-0 hXyplo") != None:
        list = soup.findAll("div", class_="sc-1g6z4xm-0 hXyplo")

        EersteVijf = list[0:5]

        for item in EersteVijf:
            item = str(item.get_text())
            hash = item.replace("Hash","").split("Time")[0]
            time = item.split("Time")[1].split("Amount (BTC)")[0]
            amount_btc = item.split("Amount (BTC)")[1].split("Amount (USD)")[0]
            amount_usd = item.split("Amount (BTC)")[1].split("Amount (USD)")[1]

            if red.get(hash) == None:
                data = {hash:{"Time":time, "Amount (BTC)": amount_btc, "Amount (USD)": amount_usd}}
                col_bitcoin.insert_one(data)

            red.set(hash, time, ex=70)

    print("Scraper uitgevoerd!")
    sleep(60)