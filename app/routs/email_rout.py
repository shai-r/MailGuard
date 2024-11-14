from dataclasses import asdict

from flask import request, jsonify, Blueprint

from app.services.kafka_services.produce_service import produce_new_email_by_topic, produce_to_sql
from app.services.terrorist_service import get_all_terrorist_by_email

emails_blueprint = Blueprint('emails', __name__)

@emails_blueprint.route('/email', methods=['POST'])
def get_emails():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        produce_new_email_by_topic(data, 'ALL_MESSAGES_TOPIC')
        produce_to_sql(data)
        return jsonify({"message": "Email received and processed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@emails_blueprint.route('/email/<string:email>', methods=['GET'])
def get_terrorist_by_email(email: str):
    x = get_all_terrorist_by_email(email)
    print(x)
    return jsonify(x), 200
