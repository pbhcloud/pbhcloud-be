
from pymongo import MongoClient
from dotenv import load_dotenv
import os
# https://github.com/mongodb-university/atlas_starter_python/blob/master/atlas-starter.py should be reviewed.

def mongoConfig():
    load_dotenv()
    uri = os.getenv('MONGO_URL')

    # TODO - Change it accordingly to whats written in main.py
    client = MongoClient(uri, tls=True)

    # # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged Mongo cluster deployment. Successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client

