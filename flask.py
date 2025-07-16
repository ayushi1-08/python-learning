from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory "database"
users = []

@app.route('/')
def home():
  return "Welcome to the homepage!"

@app.route('/users', methods=['POST'])
def create_user():
  data = request.get_json()
  users.append(data)
  return jsonify({"message": "User created", "user": data}), 201

@app.route('/users', methods=['GET'])
def get_users():
  return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
  if 0 <= user_id < len(users):
      return jsonify(users[user_id])
  return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
  if 0 <= user_id < len(users):
    data = request.get_json()
    users[user_id] = data
    return jsonify({"message": "User updated", "user": data})
  return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
  if 0 <= user_id < len(users):
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user})
  return jsonify({"error": "User not found"}), 404

# Run the server
if __name__ == '__main__':
  app.run(debug=True)
