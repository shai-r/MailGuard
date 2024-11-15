import os
import json

from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.services.explosive_sentence_service import insert_email_into_explosive_sql

load_dotenv(verbose=True)

def consume_explosive_messages():
    consumer = KafkaConsumer(
        os.environ['EXPLOSIVE_MESSAGES'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(f'Received- {message.key}: {message.value}')
        insert_email_into_explosive_sql(message.value)

if __name__ == '__main__':
    consume_explosive_messages()