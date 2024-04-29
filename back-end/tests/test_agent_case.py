def test_register_agent(mongo_db, agent_service, agent_repository, model_agent):

    agent = agent_service.register_agent(model_agent.name, model_agent.identifier)

    assert agent.name == model_agent.name
    assert agent.identifier == model_agent.identifier
    assert agent.updated_at is not None
    assert agent.id is not None


def test_find_agent_by_identifier(
    mongo_db, agent_service, agent_repository, exists_agent
):

    found_agent = agent_service.find_agent_by_identifier(exists_agent.identifier)

    assert found_agent.name == exists_agent.name
    assert found_agent.id == exists_agent.id
    assert found_agent.updated_at == exists_agent.updated_at


def test_update_agent(mongo_db, agent_service, agent_repository, exists_agent):
    new_name = "Jane Smith"

    agent_service.update_agent(new_name, exists_agent.identifier)

    updated_agent = agent_repository.get_agent_by_identifier(exists_agent.identifier)

    assert updated_agent.name == "Jane Smith"
    assert updated_agent.identifier == exists_agent.identifier
    assert updated_agent.id == exists_agent.id


def test_remove_agent(mongo_db, agent_service, agent_repository, exists_agent):

    agent_service.remove_agent(exists_agent.identifier)

    assert agent_repository.get_agent_by_identifier(exists_agent.identifier) is None
