from flask import Blueprint, request, jsonify
from application.use_cases.user_service import UserService
from application.repository.mongo_user_repository import MongoUserRepository
from mongoengine import connect

connect(
    db='test',
    username='user',
    password='123456',
    host='mongodb://user:123456@localhost/'
)
user_service = UserService(MongoUserRepository())

user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/users", methods=["GET"])
def get_users():
    users = user_service.find_all_users()
    print(users)
    return jsonify( users = [user.to_dict() for user in users])


@user_blueprint.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    # Lógica para obtener un usuario específico
    return jsonify({})


# Añadir más rutas según sea necesario