from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    name = data.get('name')
    email = data.get('email')

    if user_id in users:
        return jsonify({"error": "User ID already exists"}), 400

    users[user_id] = {"name": name, "email": email}
    return jsonify({"message": "User added", "user": users[user_id]}), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    users[user_id].update({"name": name, "email": email})
    return jsonify({"message": "User updated", "user": users[user_id]}), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"}), 200

@app.route('/')
def home():
    return "<h2> Flask User Management API is running. Use /users endpoint to interact.</h2>"
