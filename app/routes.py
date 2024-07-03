import os
import csv
from flask import Blueprint, render_template, request, jsonify, current_app

main = Blueprint('main', __name__)

# Example test Hello World
@main.route('/api', methods=['GET'])
def api_root():
    return jsonify(message="Hello, World!!")
 
# Example json list users data enpoint
@main.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ]
    return jsonify(users=users)

# Enpoint for do post verbose .csv
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify(error="No file part"), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify(error="No selected file"), 400

        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(current_app.root_path, UPLOAD_FOLDER, filename))
            return jsonify(message="File uploaded successfully", filename=filename), 201
        else:
            return jsonify(error="Allowed file types are .csv"), 400
    
    # Si es un GET, mostrar la interfaz para cargar el archivo
    return render_template('upload.html')

# Enpoint for do Get of .csv
@main.route('/data', methods=['GET'])
def get_data():
    csv_data = []
    csv_path = os.path.join(current_app.root_path, UPLOAD_FOLDER, 'data.csv')
    
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                csv_data.append(row)
    except FileNotFoundError:
        return jsonify(error="CSV file not found"), 404
    
    return jsonify(data=csv_data), 200