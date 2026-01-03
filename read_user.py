from flask import Blueprint, jsonify
from data_store import users

read_bp = Blueprint("read_bp", __name__)

@read_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)
