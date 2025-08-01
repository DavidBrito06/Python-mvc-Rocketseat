from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from src.main.routers.person_routes import person_route_bp
from src.main.routers.pets_routes import pet_router_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_router_bp)
app.register_blueprint(person_route_bp)
