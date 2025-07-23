from flask import Blueprint, jsonify

pet_router_bp = Blueprint('pet_router', __name__)

@pet_router_bp.route('/pets', methods=['GET'])
def list_pets():
    return jsonify({"message": "List of pets"}), 200