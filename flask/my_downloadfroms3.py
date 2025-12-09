from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]


@app.route("/users", methods=["GET"])
def list_users():
    return jsonify(USERS)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # Find user by id
    for user in USERS:
        if user["id"] == user_id:
            return jsonify(user)
    # If not found, return 404-style response
    return jsonify({"error": "User not found"}), 404


@app.route("/users", methods=["POST"])
def create_user():
    # Read JSON body
    data = request.get_json()

    # Very basic validation
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    new_id = len(USERS) + 1
    new_user = {"id": new_id, "name": data["name"]}
    USERS.append(new_user)

    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)
