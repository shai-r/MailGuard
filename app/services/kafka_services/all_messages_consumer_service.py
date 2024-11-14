import os
import json

from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.db.mongodb_db.mongodb_database import mongodb_messages_collection

load_dotenv(verbose=True)

def consume_all_messages():
    consumer = KafkaConsumer(
        os.environ['ALL_MESSAGES_TOPIC'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(f'Received- {message.key}: {message.value}')
        mongodb_messages_collection.insert_one(message.value)

if __name__ == '__main__':
    consume_all_messages()