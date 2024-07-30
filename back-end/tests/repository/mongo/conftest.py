import pytest

from application.repository.mongo_user_repository import MongoUserRepository
from application.repository.mongo_agent_repository import MongoAgentRepository
from application.repository.mongo_vehicle_repository import MongoVehicleRepository
from application.repository.mongo_violation_repository import MongoViolationsRepository
from application.repository.mongo_auth_repository import MongoAuthRepository
from infrastructure.localization.json_localization import JSONLocalizationAdapter



@pytest.fixture(scope="function")
def localization_adapter():
    return JSONLocalizationAdapter("en")


@pytest.fixture(scope="function")
def user_repository():
    return MongoUserRepository()


@pytest.fixture(scope="function")
def agent_repository():
    return MongoAgentRepository()


@pytest.fixture(scope="function")
def vehicle_repository():
    return MongoVehicleRepository()


@pytest.fixture(scope="function")
def violation_repository():
    return MongoViolationsRepository()


@pytest.fixture(scope="function")
def auth_repository():
    return MongoAuthRepository()


@pytest.fixture(scope="function")
def exists_user(model_user, user_repository):
    return user_repository.add_user(model_user)


@pytest.fixture(scope="function")
def exists_user_2(model_user_2, user_repository):
    return user_repository.add_user(model_user_2)


@pytest.fixture(scope="function")
def exists_vehicle(model_vehicle, vehicle_repository):
    return vehicle_repository.add_vehicle(model_vehicle)


@pytest.fixture(scope="function")
def exist_violation(model_violation, violation_repository):
    return violation_repository.add_violation(model_violation)


@pytest.fixture(scope="function")
def exist_violation_2(model_violation_2, violation_repository):
    return violation_repository.add_violation(model_violation_2)


@pytest.fixture(scope="function")
def exist_auth_agent(model_auth_agent, auth_repository):
    auth = auth_repository.add_auth(model_auth_agent)
    return auth


@pytest.fixture(scope="function")
def exist_auth_user(model_auth_user, auth_repository):
    auth = auth_repository.add_auth(model_auth_user)
    return auth

@pytest.fixture(scope="function")
def exists_agent(model_agent, agent_repository):
    agent = agent_repository.add_agent(model_agent)
    return agent
