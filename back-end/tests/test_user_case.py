from pytest import raises
from domain.models.user import User
from shared.utils.exceptions import DataValidationError, UniqueViolation, NotFoundModel


def test_register_user(mongo_db, user_service):
    name = "John Doe"
    email = "john.doe@example.com"
    new_user = user_service.register_user(name, email)
    assert new_user is not None
    assert type(new_user) == User
    assert new_user.name == name
    assert new_user.email == email


def test_register_bad_email_format(mongo_db, user_service):
    name = "John Doe"
    email = "john.doeexample.com"
    with raises(DataValidationError) as exc_info:
        user_service.register_user(name, email)
        assert exc_info.value.message == "invalid_email"


def test_register_user_email_already_exists(mongo_db, user_service, exists_user):
    with raises(UniqueViolation) as exc_info:
        user_service.register_user(exists_user.name, exists_user.email)
        assert "unique" in str(exc_info)


def test_find_user_by_email(mongo_db, user_service, exists_user):
    retrieved_user = user_service.find_user_by_email(exists_user.email)
    assert retrieved_user is not None
    assert type(retrieved_user) == User
    assert retrieved_user.email == exists_user.email


def test_find_user_by_email_not_found(mongo_db, user_service):
    with raises(NotFoundModel) as exc_info:
        user_service.find_user_by_email("not_exist@test")
        assert "user_not_found" in str(exc_info)


def test_find_all_users(mongo_db, user_service, exists_user):
    retrieved_users = user_service.find_all_users()
    assert type(retrieved_users) == list
    assert len(retrieved_users) >= 1


def test_update_user(mongo_db, user_service, exists_user):
    new_name = "Jane Doe"
    exists_user.name = new_name
    updated_user = user_service.update_user(name=new_name, email=exists_user.email)
    assert updated_user is not None
    assert type(updated_user) == User
    assert updated_user.name == new_name


def test_delete_user(mongo_db, user_service, exists_user):
    assert user_service.delete_user(exists_user.email) == None


def test_delete_user_not_found(mongo_db, user_service):
    with raises(NotFoundModel) as exc_info:
        user_service.delete_user("not_exist@test")
        assert "user_not_found" in str(exc_info)
