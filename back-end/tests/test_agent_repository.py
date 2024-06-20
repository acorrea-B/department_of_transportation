import pytest
from shared.utils.exceptions import NotFoundModel
from domain.models.agent import Agent


@pytest.fixture(scope="function")
def model_agent():
    return Agent(name="John Doe", identifier="12345")


@pytest.fixture(scope="function")
def exists_agent(model_agent, agent_repository):
    return agent_repository.add_agent(model_agent)


def test_add_agent(mongo_db, agent_repository, model_agent):

    result = agent_repository.add_agent(model_agent)

    assert isinstance(result, Agent)
    assert result.name == model_agent.name
    assert result.identifier == model_agent.identifier
    assert result.identifier is not None
    assert result.updated_at is not None


def test_get_agent_by_identifier(mongo_db, agent_repository, exists_agent):
    result = agent_repository.get_agent_by_identifier(exists_agent.identifier)

    assert isinstance(result, Agent)
    assert result.name == exists_agent.name
    assert result.identifier == exists_agent.identifier


def test_update_agent(mongo_db, agent_repository, exists_agent):
    new_name = "Jane Doe"
    exists_agent.name = new_name
    result = agent_repository.update_agent(exists_agent)

    assert isinstance(result, Agent)
    assert result.name == new_name
    assert result.identifier == exists_agent.identifier


def test_delete_agent(mongo_db, agent_repository, exists_agent):

    agent_repository.delete_agent(exists_agent.identifier)

    with pytest.raises(NotFoundModel) as excep_info:
        agent_repository.get_agent_by_identifier(exists_agent.identifier)
        assert "agent_not_found" in str(excep_info)


def test_agent_not_found_by_identifier(mongo_db, agent_repository):
    with pytest.raises(NotFoundModel) as excep_info:
        agent_repository.get_agent_by_identifier("nonexistent")
        assert "agent_not_found" in str(excep_info)


def update_agent_not_found_by_identifier(mongo_db, agent_repository, model_agent):
    result = agent_repository.update_agent(model_agent)

    assert result is None


def test_get_all_agents(mongo_db, agent_repository, exists_agent):
    result = agent_repository.get_agents()

    assert isinstance(result, list)
    assert len(result) >= 1

    for agent in result:
        assert isinstance(agent, Agent)
        assert agent.name is not None
        assert agent.identifier is not None
        assert agent.updated_at is not None
        assert agent.id is not None
