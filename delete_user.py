from flask import Blueprint, jsonify
from data_store import users

delete_bp = Blueprint("delete_bp", __name__)

@delete_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    users.pop(user_id)
    return jsonify({"message": "User deleted", "users": users})
