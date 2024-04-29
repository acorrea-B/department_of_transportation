from pytest import raises
from mongoengine import ValidationError
from domain.models.user import User


def test_register_user(mongo_db, user_service):
    name = "John Doe"
    email = "john.doe@example.com"
    new_user = user_service.register_user(name, email)
    assert new_user is not None
    assert type(new_user) == User
    assert new_user.name == name
    assert new_user.email == email

def teest_register_bad_email_format(mongo_db, user_service):
    name = "John Doe"
    email = "john.doeexample.com"
    with raises(ValidationError) as exc_info:
        new_user = user_service.register_user(name, email)
        assert exc_info.value.message == "Invalid email format"
    


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
