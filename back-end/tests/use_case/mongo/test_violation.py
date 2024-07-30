import pytest
from bson import ObjectId
from datetime import datetime, timedelta
from domain.models.vehicle import Vehicle
from shared.utils.exceptions import NotFoundModel


def test_register_violation(
    mongo_db,
    violation_service,
    model_violation,
):
    violation = violation_service.register_violation(
        model_violation.vehicle.license_plate,
        model_violation.comments,
        model_violation.timestamp,
    )

    assert violation is not None
    assert violation.vehicle.id == model_violation.vehicle.id
    assert violation.comments == model_violation.comments
    assert violation.timestamp[:18] == model_violation.timestamp[:18]

def test_register_violation_vehicle_not_exist(
    mongo_db,
    violation_service,
    model_violation
):
    with pytest.raises(NotFoundModel) as exc_info:
        violation_service.register_violation(
        "not_exits",
        model_violation.comments,
        model_violation.timestamp,
    )
        assert exc_info.value.message == "viol_not_found"

def test_get_violations_by_vehicle(
    mongo_db,
    violation_service,
    exist_violation,
    exist_violation_2,
):

    violations = violation_service.get_violations_by_vehicle(
        exist_violation.vehicle.license_plate
    )

    assert len(violations) == 2
    for violation in violations:
        assert violation.vehicle.id == exist_violation.vehicle.id
        assert violation.comments in [
            exist_violation.comments,
            exist_violation_2.comments,
        ]
        assert violation.timestamp in [
            exist_violation.timestamp,
            exist_violation_2.timestamp,
        ]


def test_get_violation(
    mongo_db,
    violation_service,
    exist_violation,
):
    violation = violation_service.get_violation(exist_violation.id)

    assert violation is not None
    assert violation.vehicle.id == exist_violation.vehicle.id
    assert violation.comments == exist_violation.comments
    assert violation.timestamp == exist_violation.timestamp


def test_get_violation_not_found(
    mongo_db,
    violation_service,
):
    with pytest.raises(NotFoundModel) as exc_info:
        violation_service.get_violation(str(ObjectId()))
        assert exc_info.value.message == "violation_not_found"


def test_get_all_violations(
    mongo_db,
    violation_service,
    exist_violation,
    exist_violation_2,
):
    violations = violation_service.get_all_violations()

    assert len(violations) == 2
    for violation in violations:
        assert violation.vehicle.id in [
            exist_violation.vehicle.id,
            exist_violation_2.vehicle.id,
        ]
        assert violation.comments in [
            exist_violation.comments,
            exist_violation_2.comments,
        ]
        assert violation.timestamp in [
            exist_violation.timestamp,
            exist_violation_2.timestamp,
        ]


def test_update_violation(
    mongo_db,
    violation_service,
    exist_violation,
):
    exist_violation.comments = "New comments"
    exist_violation.timestamp = datetime.now() + timedelta(days=1)

    violation = violation_service.update_violation(exist_violation)

    assert violation is not None
    assert violation.vehicle.id == exist_violation.vehicle.id
    assert violation.comments == exist_violation.comments
    assert violation.timestamp == exist_violation.timestamp


def test_update_violation_not_exist(
    mongo_db,
    violation_service,
    exist_violation,
):

    exist_violation.id = str(ObjectId())
    with pytest.raises(NotFoundModel) as exc_info:
        violation_service.update_violation(exist_violation)
        assert exc_info.value.message == "violation_not_found"


def test_delete_violation(
    mongo_db,
    violation_service,
    exist_violation,
):
    violation_service.delete_violation(exist_violation.id)

    with pytest.raises(NotFoundModel) as exc_info:
        violation_service.get_violation(exist_violation.id)
        assert exc_info.value.message == "violation_not_found"


def test_delete_violation_not_exist(mongo_db, violation_service):
    with pytest.raises(NotFoundModel) as exc_info:
        violation_service.get_violation(str(ObjectId()))
        assert exc_info.value.message == "violation_not_found"
