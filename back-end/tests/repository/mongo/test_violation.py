from pytest import raises
from datetime import datetime, timedelta
from application.repository.mongo_violation_repository import MongoViolationsRepository
from shared.utils.exceptions import NotFoundModel


def test_add_violation(mongo_db, model_violation, violation_repository):

    added_violation = violation_repository.add_violation(model_violation)
    assert added_violation is not None
    assert (
        added_violation.vehicle.license_plate == model_violation.vehicle.license_plate
    )
    assert added_violation.comments == model_violation.comments
    assert added_violation.timestamp == model_violation.timestamp
    assert added_violation.id is not None


def test_get_violations_by_vehicle(
    mongo_db, violation_repository, exist_violation, exist_violation_2
):

    violations = violation_repository.get_violations_by_vehicle(
        exist_violation.vehicle.id
    )

    assert len(violations) == 2
    assert violations[0].vehicle.license_plate == exist_violation.vehicle.license_plate
    assert violations[0].comments == exist_violation.comments
    assert violations[0].timestamp == exist_violation.timestamp
    assert (
        violations[1].vehicle.license_plate == exist_violation_2.vehicle.license_plate
    )
    assert violations[1].comments == exist_violation_2.comments
    assert violations[1].timestamp == exist_violation_2.timestamp


def test_get_all_violations(
    mongo_db, violation_repository, exist_violation, exist_violation_2
):

    violations = violation_repository.get_all_violations()

    assert len(violations) == 2
    for violation in violations:
        assert violation.vehicle.license_plate in [
            exist_violation.vehicle.license_plate,
            exist_violation_2.vehicle.license_plate,
        ]
        assert violation.comments in [
            exist_violation.comments,
            exist_violation_2.comments,
        ]
        assert violation.timestamp in [
            exist_violation.timestamp,
            exist_violation_2.timestamp,
        ]


def test_update_violation(mongo_db, violation_repository, exist_violation):
    new_comments = "Running a red light and speeding"
    new_timestamp = datetime.now() + timedelta(days=1)

    exist_violation.comments = new_comments
    exist_violation.timestamp = new_timestamp

    violation_repository.update_violation(exist_violation)

    retrieved_violation = violation_repository.get_violation_by_id(
        exist_violation.id
    )
    assert retrieved_violation is not None
    assert (
        retrieved_violation.vehicle.license_plate
        == exist_violation.vehicle.license_plate
    )
    assert retrieved_violation.comments == new_comments
    assert retrieved_violation.timestamp == exist_violation.timestamp
    assert retrieved_violation.id == exist_violation.id


def test_delete_violation(mongo_db, violation_repository, exist_violation):

    violation_repository.delete_violation(exist_violation.id)

    with raises(NotFoundModel) as exception_info:
        violation_repository.get_violation_by_id(exist_violation.id)
        assert exception_info.value == "violation_not_found"
