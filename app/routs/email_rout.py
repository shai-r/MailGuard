from flask import request, jsonify, Blueprint

emails_blueprint = Blueprint('emails', __name__)

@emails_blueprint.route('/email', methods=['POST'])
def receive_email():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        return jsonify({"message": "Email received and processed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500