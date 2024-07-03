from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/api', methods=['GET'])
def api_root():
    return jsonify(message="Hello, World!!")
 