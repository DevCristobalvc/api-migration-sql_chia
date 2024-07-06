import os
import json
from flask import Blueprint, request, jsonify, current_app

main = Blueprint('main', __name__)

DATA_FILE = 'data.json'

# Cargar datos desde el archivo JSON
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"holders": [], "initiatives": []}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Guardar datos en el archivo JSON
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Rutas para la tabla 'holders'
@main.route('/holders', methods=['GET'])
def get_holders():
    data = load_data()
    return jsonify(data['holders'])

@main.route('/holders', methods=['POST'])
def create_holder():
    new_holder = request.json
    data = load_data()
    data['holders'].append(new_holder)
    save_data(data)
    return jsonify(new_holder), 201

@main.route('/holders/<int:id>', methods=['GET'])
def get_holder(id):
    data = load_data()
    holder = next((h for h in data['holders'] if h['id'] == id), None)
    if holder is None:
        return jsonify({"error": "Holder not found"}), 404
    return jsonify(holder)

@main.route('/holders/<int:id>', methods=['PUT'])
def update_holder(id):
    updated_holder = request.json
    data = load_data()
    holder = next((h for h in data['holders'] if h['id'] == id), None)
    if holder is None:
        return jsonify({"error": "Holder not found"}), 404
    holder.update(updated_holder)
    save_data(data)
    return jsonify(holder)

@main.route('/holders/<int:id>', methods=['DELETE'])
def delete_holder(id):
    data = load_data()
    holder = next((h for h in data['holders'] if h['id'] == id), None)
    if holder is None:
        return jsonify({"error": "Holder not found"}), 404
    data['holders'].remove(holder)
    save_data(data)
    return '', 204

# Rutas para la tabla 'initiatives'
@main.route('/initiatives', methods=['GET'])
def get_initiatives():
    data = load_data()
    return jsonify(data['initiatives'])

@main.route('/initiatives', methods=['POST'])
def create_initiative():
    new_initiative = request.json
    data = load_data()
    data['initiatives'].append(new_initiative)
    save_data(data)
    return jsonify(new_initiative), 201

@main.route('/initiatives/<int:id>', methods=['GET'])
def get_initiative(id):
    data = load_data()
    initiative = next((i for i in data['initiatives'] if i['id'] == id), None)
    if initiative is None:
        return jsonify({"error": "Initiative not found"}), 404
    return jsonify(initiative)

@main.route('/initiatives/<int:id>', methods=['PUT'])
def update_initiative(id):
    updated_initiative = request.json
    data = load_data()
    initiative = next((i for i in data['initiatives'] if i['id'] == id), None)
    if initiative is None:
        return jsonify({"error": "Initiative not found"}), 404
    initiative.update(updated_initiative)
    save_data(data)
    return jsonify(initiative)

@main.route('/initiatives/<int:id>', methods=['DELETE'])
def delete_initiative(id):
    data = load_data()
    initiative = next((i for i in data['initiatives'] if i['id'] == id), None)
    if initiative is None:
        return jsonify({"error": "Initiative not found"}), 404
    data['initiatives'].remove(initiative)
    save_data(data)
    return '', 204

# Example test Hello World
@main.route('/api', methods=['GET'])
def api_root():
    return jsonify(message="Hello, World!!")

# Example json list users data endpoint
@main.route('/users', methods=['GET'])
def list_users():
    users = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]
    return jsonify(users)
