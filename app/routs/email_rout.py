from flask import request, jsonify, Blueprint

from app.services.kafka_services.produce_service import produce_new_email_by_topic, produce_to_sql

emails_blueprint = Blueprint('emails', __name__)

@emails_blueprint.route('/email', methods=['POST'])
def receive_email():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        produce_new_email_by_topic(data, 'ALL_MESSAGES_TOPIC')
        produce_to_sql(data)
        return jsonify({"message": "Email received and processed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500