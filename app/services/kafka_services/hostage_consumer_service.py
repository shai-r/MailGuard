import os
import json

from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.services.hostage_sentence_service import insert_email_into_hostage_sql

load_dotenv(verbose=True)

def consume_hostage_messages():
    consumer = KafkaConsumer(
        os.environ['HOSTAGE_MESSAGES'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(f'Received- {message.key}: {message.value}')
        insert_email_into_hostage_sql(message.value)

if __name__ == '__main__':
    consume_hostage_messages()