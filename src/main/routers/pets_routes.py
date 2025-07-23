from flask import Blueprint, jsonify
from src.main.composer.pet_lister_view_composer import pet_lister_composer
from src.main.composer.pet_delete_composer import pet_delete_composer
from src.views.http_types.http_request import HttpRequest

pet_router_bp = Blueprint('pet_router', __name__)

@pet_router_bp.route('/pets', methods=['GET'])
def list_pets():
    http_request = HttpRequest()
    view = pet_lister_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pet_router_bp.route('/pets/<name>', methods=['DELETE'])
def delete_pet(name):
    http_request = HttpRequest(param={'name': name})
    view = pet_delete_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code