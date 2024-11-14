import os

from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic

load_dotenv(verbose=True)

topics = [
    {
        "name": os.environ['ALL_MESSAGES_TOPIC'],
        "partitions": int(os.environ['NUM_PARTITIONS']),
        "replication": int(os.environ['REPLICATION_FACTOR'])
    },
    {
        "name": os.environ['HOSTAGE_MESSAGES'],
        "partitions": int(os.environ['NUM_PARTITIONS']),
        "replication": int(os.environ['REPLICATION_FACTOR'])
    },
    {
        "name": os.environ['EXPLOSIVE_MESSAGES'],
        "partitions": int(os.environ['NUM_PARTITIONS']),
        "replication": int(os.environ['REPLICATION_FACTOR'])
    }
]

def init_topics():
    admin_client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])

    topic_list = [
        NewTopic(
            name=topic["name"],
            num_partitions=topic["partitions"],
            replication_factor=topic["replication"]
        )
        for topic in topics
    ]

    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print("Topics created successfully!")
    except Exception as e:
        print(f"Error creating topics: {e}")
    finally:
        admin_client.close()
