import os
import json
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv(verbose=True)

def produce_new_email_by_topic(new_email: dict, topic: str):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(
        os.environ[topic],
        value=new_email,
        key=new_email['email'].encode('utf-8')
    )
    producer.flush()
    print(f'Send: {new_email}')