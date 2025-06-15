#i ran this code on google colab

from pymongo.mongo_client import MongoClient
import pandas as pd
import json


#url
uri="mongodb+srv://ishikkaaa:helloworld@cluster0.phyllcr.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to server
client=MongoClient(uri)

#create db name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

df=pd.read_csv('./notebooks/wafer_23012020_041211.csv')

df.head()
df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)