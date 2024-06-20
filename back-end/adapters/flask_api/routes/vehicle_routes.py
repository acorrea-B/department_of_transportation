from flask import Blueprint, request, jsonify, current_app
from adapters.flask_api.inputs.vehicle_input import CreateVehicleForm, UpdateVehicleForm
from shared.utils.exceptions import NotFoundModel, UniqueViolation


vehicle_blueprint = Blueprint("vehicle_blueprint", __name__)
dependencies = lambda dependencie: getattr(
    current_app.blueprints["vehicle_blueprint"].dependencie_container, dependencie
)


@vehicle_blueprint.route("/vehicles", methods=["GET"])
def get_vehicles():
    """
    Retrieve all vehicles.

    Returns:
        A JSON response containing a list of vehicles and a message.
    """
    vehicle_service = dependencies("service_vehicle")
    localization = dependencies("localization")
    vehicles = vehicle_service.find_all_vehicles()
    return (
        jsonify(
            vehicles=[vehicle.to_dict() for vehicle in vehicles],
            message=localization.get_message("vehicle_read"),
        ),
        200,
    )


@vehicle_blueprint.route("/vehicles/<string:email>", methods=["GET"])
def get_vehicle(email):
    """
    Retrieve a vehicle by email.

    Args:
        email (str): The email of the vehicle.

    Returns:
        A JSON response containing the vehicle and a message.

    Raises:
        NotFoundModel: If the vehicle is not found.
    """
    vehicle_service = dependencies("service_vehicle")
    localization = dependencies("localization")
    try:
        vehicle = vehicle_service.find_vehicle_by_email(email)
        return (
            jsonify(vehicle=vehicle.to_dict(), message=localization.get_message("vehicle_read")),
            200,
        )
    except NotFoundModel:
        return jsonify(vehicle={}, message=localization.get_message("vehicle_not_found"))


@vehicle_blueprint.route("/vehicles", methods=["POST"])
def register_vehicle():
    """
    Register a new vehicle.

    Returns:
        A JSON response containing the created vehicle and a message.

    Raises:
        UniqueViolation: If the vehicle already exists.
    """
    vehicle_service = dependencies("service_vehicle")
    localization = dependencies("localization")
    form = vehicleForm(formdata=request.form, data=request.get_json())
    if not form.validate():
        return jsonify(vehicle={}, message=form.errors), 400
    try:
        vehicle = vehicle_service.register_vehicle(form.name.data, form.email.data)
        return (
            jsonify(
                vehicle=vehicle.to_dict(), message=localization.get_message("vehicle_created")
            ),
            200,
        )
    except UniqueViolation as e:
        return jsonify(vehicle={}, message=localization.get_message("vehicle_exists")), 409


@vehicle_blueprint.route("/vehicles", methods=["PUT"])
def update_vehicle():
    """
    Update a vehicle.

    Returns:
        A JSON response containing the updated vehicle and a message.

    Raises:
        NotFoundModel: If the vehicle is not found.
    """
    vehicle_service = dependencies("service_vehicle")
    localization = dependencies("localization")
    form = vehicleForm(formdata=request.form, data=request.get_json())
    if not form.validate():
        return jsonify(vehicle={}, message=form.errors), 400
    try:
        vehicle = vehicle_service.update_vehicle(form.name.data, form.email.data)
        return jsonify(
            vehicle=vehicle.to_dict(), message=localization.get_message("vehicle_updated")
        )
    except NotFoundModel:
        return jsonify(vehicle={}, message=localization.get_message("vehicle_not_found")), 404


@vehicle_blueprint.route("/vehicles/<string:email>", methods=["DELETE"])
def delete_vehicle(email):
    """
    Delete a vehicle by email.

    Args:
        email (str): The email of the vehicle to delete.

    Returns:
        A JSON response containing a message.

    Raises:
        NotFoundModel: If the vehicle is not found.
    """
    vehicle_service = dependencies("service_vehicle")
    localization = dependencies("localization")
    try:
        vehicle_service.delete_vehicle(email)
        return jsonify(vehicle={}, message=localization.get_message("vehicle_deleted")), 200
    except NotFoundModel:
        return jsonify(vehicle={}, message=localization.get_message("vehicle_not_found")), 404
