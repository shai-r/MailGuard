from flask import Flask

from app.db.mongodb.mongodb_database import mongodb_messages_collection
from app.routs.email_rout import emails_blueprint
from app.services.kafka_services.admin_service import init_topics

app = Flask(__name__)

if __name__ == '__main__':
    # init_postgresql()
    mongodb_messages_collection.drop()
    init_topics()
    app.register_blueprint(emails_blueprint, url_prefix="/api")
    app.run(host='localhost', port=5000)
