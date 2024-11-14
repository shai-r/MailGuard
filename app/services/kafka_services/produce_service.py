import os
import json
from dotenv import load_dotenv
from kafka import KafkaProducer

from app.utils.sentence_utils import order_sentences, is_hostage_in_sentence, is_explos_in_sentence

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

def produce_to_sql(email: dict):
    sentences = order_sentences(email['sentences']) if 'sentences' in email.keys() else None
    is_hostage = is_hostage_in_sentence(sentences[0])
    is_explos = is_explos_in_sentence(sentences[0])

    if is_hostage:
        produce_new_email_by_topic({**email, 'sentences': sentences},'HOSTAGE_MESSAGES')

    if is_explos:
        produce_new_email_by_topic({**email, 'sentences': sentences}, 'EXPLOSIVE_MESSAGES')