# /app/api/user_routes.py
from flask import Blueprint, request, jsonify
from application.use_cases.user_service import UserService
from application.repository.mongo_user_repository import MongoUserRepository

user_service = UserService(MongoUserRepository)

user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/users", methods=["GET"])
def get_users():
    # Lógica para obtener usuarios
    return jsonify([])


@user_blueprint.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # Lógica para obtener un usuario específico
    return jsonify({})


# Añadir más rutas según sea necesario
