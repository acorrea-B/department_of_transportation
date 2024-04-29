from domain.models.user import User


def test_add_user(mongo_db, user_repository, model_user):
    retrieved_user = user_repository.add_user(model_user)
    assert retrieved_user is not None
    assert type(retrieved_user) == User
    assert retrieved_user.name == "John Doe"
    assert retrieved_user.email == "john.doe@example.com"


def test_email_already_exists(mongo_db, exists_user, user_repository):
    retrieved_user = user_repository.add_user(exists_user)
    assert retrieved_user is None


def test_get_user_by_email(mongo_db, exists_user, user_repository):
    retrieved_user = user_repository.get_user_by_email(exists_user.email)
    assert retrieved_user is not None
    assert type(retrieved_user) == User
    assert retrieved_user.name == exists_user.name
    assert retrieved_user.email == exists_user.email


def test_update_user(mongo_db, exists_user, user_repository):
    new_name = "Jane Doe"
    exists_user.name = new_name
    retrieved_user = user_repository.update_user(exists_user)
    assert retrieved_user is not None
    assert type(retrieved_user) == User
    assert retrieved_user.name == new_name


def test_user_not_found_by_email(mongo_db, user_repository):
    retrieved_user = user_repository.get_user_by_email("nonexistent@example.com")
    assert retrieved_user is None


def test_delete_user(mongo_db, exists_user, user_repository):
    user_repository.delete_user(exists_user.email)
    retrieved_user = user_repository.get_user_by_email(exists_user.email)
    assert retrieved_user is None


def test_find_all_users(mongo_db, exists_user, user_repository):
    retrieved_users = user_repository.get_users()
    assert type(retrieved_users) == list
    assert len(retrieved_users) >= 1
    for user in retrieved_users:
        assert type(user) == User
        assert user.name is not None
        assert user.email is not None
        assert user.id is not None
        assert user.updated_at is not None
