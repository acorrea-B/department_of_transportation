import pytest
from application.use_cases.vehicle_service import VehicleService
from domain.models.vehicle import Vehicle
from shared.utils.exceptions import NotFoundModel


def test_register_vehicle(
    mongo_db,
    vehicle_service,
    model_vehicle,
):

    vehicle = vehicle_service.register_vehicle(
        model_vehicle.license_plate,
        model_vehicle.brand,
        model_vehicle.color,
        model_vehicle.owner.email,
    )

    assert vehicle is not None
    assert vehicle.license_plate == model_vehicle.license_plate
    assert vehicle.brand == model_vehicle.brand
    assert vehicle.color == model_vehicle.color
    assert vehicle.owner.email == model_vehicle.owner.email


def test_register_vehicle_not_found_owner(
    mongo_db, vehicle_service, model_vehicle, localization_adapter
):
    with pytest.raises(NotFoundModel) as exception_info:
        vehicle_service.register_vehicle(
            model_vehicle.license_plate,
            model_vehicle.brand,
            model_vehicle.color,
            "not_exist@test",
        )
        assert localization_adapter.get_text("user_not_found") in str(
            exception_info.value
        )


def test_find_vehicle_by_plate(mongo_db, vehicle_service, exists_vehicle):

    found_vehicle = vehicle_service.find_vehicle_by_plate(exists_vehicle.license_plate)

    assert isinstance(found_vehicle, Vehicle)
    assert found_vehicle.license_plate == exists_vehicle.license_plate
    assert found_vehicle.brand == exists_vehicle.brand
    assert found_vehicle.color == exists_vehicle.color
    assert found_vehicle.owner.email == exists_vehicle.owner.email


def test_update_vehicle_info(mongo_db, vehicle_service, exists_vehicle, exists_user_2):
    new_color = "Blue"

    vehicle_updated = vehicle_service.update_vehicle_info(
        exists_vehicle.license_plate, new_color, exists_user_2.email
    )

    assert vehicle_updated is not None
    assert vehicle_updated.color == new_color
    assert vehicle_updated.owner.email == exists_user_2.email


def test_update_vehicle_info_not_found(
    mongo_db, vehicle_service, exists_vehicle, exists_user_2, localization_adapter
):
    new_color = "Blue"
    with pytest.raises(NotFoundModel) as exception_info:
        vehicle_updated = vehicle_service.update_vehicle_info(
            "nonexistent", new_color, exists_user_2.email
        )
        assert localization_adapter.get_text("vehicle_not_found") in str(
            exception_info.value
        )


def test_update_vehicle_info_not_found_owner(
    mongo_db, vehicle_service, exists_vehicle, exists_user_2, localization_adapter
):
    new_color = "Blue"
    with pytest.raises(NotFoundModel) as exception_info:
        vehicle_updated = vehicle_service.update_vehicle_info(
            exists_vehicle.license_plate, new_color, "not_exist@test"
        )
        assert localization_adapter.get_text("user_not_found") in str(
            exception_info.value
        )


def test_vehicle_not_found_by_plate(mongo_db, vehicle_service):

    found_vehicle = vehicle_service.find_vehicle_by_plate("nonexistent")

    assert found_vehicle is None


def test_find_all_vehicles(mongo_db, vehicle_service, exists_vehicle):

    vehicles = vehicle_service.find_all_vehicles()

    assert type(vehicles) == list
    assert len(vehicles) >= 1
    for vehicle in vehicles:
        assert type(vehicle) == Vehicle
        assert vehicle.license_plate is not None
        assert vehicle.brand is not None
        assert vehicle.color is not None
        assert vehicle.owner is not None
        assert vehicle.id is not None
        assert vehicle.updated_at is not None


def test_remove_vehicle(mongo_db, vehicle_service, exists_vehicle):

    vehicle_service.remove_vehicle(exists_vehicle.license_plate)

    removed_vehicle = vehicle_service.find_vehicle_by_plate(
        exists_vehicle.license_plate
    )
    assert removed_vehicle is None
