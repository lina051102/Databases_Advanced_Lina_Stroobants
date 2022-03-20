import requests
from time import sleep
from bs4 import BeautifulSoup
from os.path import exists
import pymongo as mongo
import pandas as pd
import redis


while True:

    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text,features="html5lib")

    if exists("BitcoinScraping.json"):
        file = open("BitcoinScraping.json",'r')
        oldJsonFile = file.read()
        file.close()
    else:
        file = open("BitcoinScraping.json",'w')
        oldJsonFile = ""
        file.close()

    if soup.find("div", class_="sc-1g6z4xm-0 hXyplo") != None:
        list = soup.findAll("div", class_="sc-1g6z4xm-0 hXyplo")
        newJsonFile = ""

        for item in list:
            item = str(item.get_text())

            hash = item.replace("Hash","").split("Time")[0]
            time = item.split("Time")[1].split("Amount (BTC)")[0]
            amount_btc = item.split("Amount (BTC)")[1].split("Amount (USD)")[0]
            amount_usd = item.split("Amount (BTC)")[1].split("Amount (USD)")[1]

            newJsonFile += ',{' + f'"Hash":"{hash}","Time":"{time}","Amount (BTC)":"{amount_btc}","Amount (USD)":"{amount_usd}"' + '}'

    if oldJsonFile == "":
        newJsonFile = newJsonFile.replace(",{","{",1)

    file = open("BitcoinScraping.json",'w')
    writeText = "[" + oldJsonFile.replace('[','').replace(']','') + newJsonFile + "]"
    file.write(writeText)
    file.close()

    #Stap 1
    json_file = "BitcoinScraping.json"
    json_file2 = pd.read_json(json_file, convert_dates=True)

    #Stap 2
    # Connecting to database
    client = mongo.MongoClient("mongodb://127.0.0.1:27017")

    # Make new database
    my_bit_database = client["Scraper"]

    json_data = json_file2[0:5].to_dict("lines")

    # Setting collumn
    col_bitcoin = my_bit_database["BitcoinData"]

    # Inserting data
    insert_data = col_bitcoin.insert_one(json_data)

    print("Scraper uitgevoerd!")
    sleep(60)