from flask import Blueprint, request, jsonify, current_app
from adapters.flask_api.inputs.user_input import UserForm
from shared.utils.exceptions import NotFoundModel, UniqueViolation


user_blueprint = Blueprint("user_blueprint", __name__)
dependencies = lambda dependencie: getattr(
    current_app.blueprints["user_blueprint"].dependencie_container, dependencie
)


@user_blueprint.route("/users", methods=["GET"])
def get_users():
    """
    Retrieve all users.

    Returns:
        A JSON response containing a list of users and a message.
    """
    user_service = dependencies("service_user")
    localization = dependencies("localization")
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
    """
    Retrieve a user by email.

    Args:
        email (str): The email of the user.

    Returns:
        A JSON response containing the user and a message.

    Raises:
        NotFoundModel: If the user is not found.
    """
    user_service = dependencies("service_user")
    localization = dependencies("localization")
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
    """
    Register a new user.

    Returns:
        A JSON response containing the created user and a message.

    Raises:
        UniqueViolation: If the user already exists.
    """
    user_service = dependencies("service_user")
    localization = dependencies("localization")
    form = UserForm(formdata=request.form, data=request.get_json())
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
    """
    Update a user.

    Returns:
        A JSON response containing the updated user and a message.

    Raises:
        NotFoundModel: If the user is not found.
    """
    user_service = dependencies("service_user")
    localization = dependencies("localization")
    form = UserForm(formdata=request.form, data=request.get_json())
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
    """
    Delete a user by email.

    Args:
        email (str): The email of the user to delete.

    Returns:
        A JSON response containing a message.

    Raises:
        NotFoundModel: If the user is not found.
    """
    user_service = dependencies("service_user")
    localization = dependencies("localization")
    try:
        user_service.delete_user(email)
        return jsonify(user={}, message=localization.get_message("user_deleted")), 200
    except NotFoundModel:
        return jsonify(user={}, message=localization.get_message("user_not_found")), 404
