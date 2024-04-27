import pytest
from domain.models.user import User
from application.use_cases.user_service import UserService


@pytest.fixture(scope="function")
def user_service(user_repository):
    return UserService(user_repository)


@pytest.fixture(scope="function")
def model_user():
    return User(name="John Doe", email="john.doe@example.com")


@pytest.fixture(scope="function")
def exists_user(model_user, user_repository):
    return user_repository.add_user(model_user)


def test_register_user(mongo_db, user_service):
    name = "John Doe"
    email = "john.doe@example.com"
    new_user = user_service.register_user(name, email)
    assert new_user is not None
    assert type(new_user) == User
    assert new_user.name == name
    assert new_user.email == email


def test_find_user_by_email(mongo_db, user_service, exists_user):
    retrieved_user = user_service.find_user_by_email(exists_user.email)
    assert retrieved_user is not None
    assert type(retrieved_user) == User
    assert retrieved_user.email == exists_user.email


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
