from domain.models.vehicle import Vehicle


def test_add_vehicle(mongo_db, vehicle_repository, model_vehicle):
    added_vehicle = vehicle_repository.add_vehicle(model_vehicle)

    assert added_vehicle is not None
    assert added_vehicle.license_plate == model_vehicle.license_plate
    assert added_vehicle.brand == model_vehicle.brand
    assert added_vehicle.color == model_vehicle.color
    assert added_vehicle.owner.email == model_vehicle.owner.email


def test_get_vehicle_by_license_plate(mongo_db, vehicle_repository, model_vehicle):
    added_vehicle = vehicle_repository.add_vehicle(model_vehicle)

    retrieved_vehicle = vehicle_repository.get_vehicle_by_license_plate(
        model_vehicle.license_plate
    )

    assert retrieved_vehicle is not None
    assert retrieved_vehicle.license_plate == added_vehicle.license_plate
    assert retrieved_vehicle.brand == added_vehicle.brand
    assert retrieved_vehicle.color == added_vehicle.color
    assert added_vehicle.owner.email == model_vehicle.owner.email


def test_update_vehicle(
    mongo_db, vehicle_repository, model_vehicle, exists_vehicle, exists_user
):

    new_brand = "Ford"
    new_color = "Blue"
    exists_vehicle.brand = new_brand
    exists_vehicle.color = new_color
    vehicle_repository.update_vehicle(exists_vehicle)

    retrieved_vehicle = vehicle_repository.get_vehicle_by_license_plate(
        model_vehicle.license_plate
    )

    assert retrieved_vehicle is not None
    assert retrieved_vehicle.license_plate == exists_vehicle.license_plate
    assert retrieved_vehicle.brand == new_brand
    assert retrieved_vehicle.color == new_color
    assert exists_vehicle.owner.email == model_vehicle.owner.email


def test_delete_vehicle(mongo_db, vehicle_repository, exists_vehicle):

    result = vehicle_repository.delete_vehicle(exists_vehicle.license_plate)

    assert result is True
    assert (
        vehicle_repository.get_vehicle_by_license_plate(exists_vehicle.license_plate)
        is None
    )


def test_get_all_vehicles(mongo_db, vehicle_repository, exists_vehicle):

    vehicles = vehicle_repository.get_all_vehicles()

    assert len(vehicles) >= 1
    for vehicle in vehicles:
        assert type(vehicle) == Vehicle
        assert vehicle.license_plate is not None
        assert vehicle.brand is not None
        assert vehicle.color is not None
        assert vehicle.owner is not None
        assert vehicle.owner.email is not None
        assert vehicle.owner.name is not None
        assert vehicle.owner.id is not None
        assert vehicle.id is not None
        assert vehicle.updated_at is not None
