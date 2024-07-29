import pytest
from shared.utils.exceptions import NotFoundModel
from domain.models.auth import Auth


def test_add_agent(mongo_db, auth_repository, model_auth_agent):

    result = auth_repository.add_auth(model_auth_agent)

    assert isinstance(result, Auth)
    assert result.username == model_auth_agent.username
    assert result.password == model_auth_agent.password
    assert result.user_id is not None
    assert result.agent_id == model_auth_agent.agent_id


def test_get_auth(mongo_db, auth_repository, exist_auth_agent):
    result = auth_repository.get_auth(
        exist_auth_agent.username, exist_auth_agent.password
    )

    assert isinstance(result, Auth)
    assert result.username == exist_auth_agent.username
    assert result.password == exist_auth_agent.password
    assert result.user_id is not None
    assert result.agent_id == exist_auth_agent.agent_id


def test_delete_auth(mongo_db, auth_repository, exist_auth_agent):

    auth_repository.delete_auth(exist_auth_agent.username)

    with pytest.raises(NotFoundModel) as excep_info:
        auth_repository.get_auth(exist_auth_agent.username, exist_auth_agent.password)
        assert "auth_not_found" in str(excep_info)


def test_auth_not_found_wrong_username_and_password(mongo_db, auth_repository):
    with pytest.raises(NotFoundModel) as excep_info:
        auth_repository.get_auth("nonexistent", "WRONG_PASSWORD")
        assert "auth_not_found" in str(excep_info)


def test_auth_not_found_wrong_username(mongo_db, auth_repository, exist_auth_agent):
    with pytest.raises(NotFoundModel) as excep_info:
        auth_repository.get_auth("nonexistent", exist_auth_agent.password)
        assert "auth_not_found" in str(excep_info)


def test_auth_not_found_wrong_password(mongo_db, auth_repository, exist_auth_agent):
    with pytest.raises(NotFoundModel) as excep_info:
        auth_repository.get_auth(exist_auth_agent.username, "WRONG_PASSWORD")
        assert "auth_not_found" in str(excep_info)
