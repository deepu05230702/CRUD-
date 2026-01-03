from flask import Blueprint, request, jsonify
from data_store import users

create_bp = Blueprint("create_bp", __name__)

@create_bp.route("/users", methods=["POST"])
def create_user():
    users.append(request.json)
    return jsonify({"message": "User added", "users": users})
