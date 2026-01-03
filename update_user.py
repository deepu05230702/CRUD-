from flask import Blueprint, request, jsonify
from data_store import users

update_bp = Blueprint("update_bp", __name__)

@update_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    users[user_id] = request.json
    return jsonify({"message": "User updated", "users": users})
