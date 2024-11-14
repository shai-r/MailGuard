import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)


mongodb_client = MongoClient(os.environ['MONGODB_URL'])
mongodb_db = mongodb_client[os.environ['DB_NAME']]
mongodb_messages_collection = mongodb_db[os.environ['MESSAGES']]