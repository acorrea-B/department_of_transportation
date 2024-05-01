from flask import Blueprint, request, jsonify
from application.use_cases.user_service import UserService
from application.repository.mongo_user_repository import MongoUserRepository
from adapters.flask_api.inputs.user_input import RegisterUserForm
from shared.utils.exceptions import NotFoundModel, UniqueViolation
from infrastructure.localization.json_localization import JSONLocalizationAdapter

user_service = UserService(MongoUserRepository())
localization = JSONLocalizationAdapter("en", "shared/localization/")
user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/users", methods=["GET"])
def get_users():
    users = user_service.find_all_users()
    return (
        jsonify(
            users=[user.to_dict() for user in users],
            message=localization.get_message("user_read"),
        ),
        200,
    )


@user_blueprint.route("/users/<string:email>", methods=["GET"])
def get_user(email):
    try:
        user = user_service.find_user_by_email(email)
        return (
            jsonify(user=user.to_dict(), message=localization.get_message("user_read")),
            200,
        )
    except NotFoundModel:
        return jsonify(user={}, message=localization.get_message("user_not_found"))


@user_blueprint.route("/users", methods=["POST"])
def register_user():
    form = RegisterUserForm(formdata=request.form, data=request.get_json())
    if not form.validate():
        return jsonify(user={}, message=form.errors), 400
    try:
        user = user_service.register_user(form.name.data, form.email.data)
        return (
            jsonify(
                user=user.to_dict(), message=localization.get_message("user_created")
            ),
            200,
        )
    except UniqueViolation as e:
        return jsonify(user={}, message=localization.get_message("user_exists")), 409


@user_blueprint.route("/users", methods=["PUT"])
def update_user():
    form = RegisterUserForm(formdata=request.form, data=request.get_json())
    if not form.validate():
        return jsonify(user={}, message=form.errors), 400
    try:
        user = user_service.update_user(form.name.data, form.email.data)
        return jsonify(
            user=user.to_dict(), message=localization.get_message("user_updated")
        )
    except NotFoundModel:
        return jsonify(user={}, message=localization.get_message("user_not_found")), 404


@user_blueprint.route("/users/<string:email>", methods=["DELETE"])
def delete_user(email):
    try:
        user_service.delete_user(email)
        return jsonify(user={}, message=localization.get_message("user_deleted")), 200
    except NotFoundModel:
        return jsonify(user={}, message=localization.get_message("user_not_found")), 404
