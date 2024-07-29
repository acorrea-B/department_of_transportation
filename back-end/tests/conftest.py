import pytest
import mongomock
from datetime import datetime
from mongoengine import connect, disconnect
from application.repository.mongo_user_repository import MongoUserRepository
from application.repository.mongo_agent_repository import MongoAgentRepository
from application.repository.mongo_vehicle_repository import MongoVehicleRepository
from application.repository.mongo_violation_repository import MongoViolationsRepository
from application.repository.mongo_auth_repository import MongoAuthRepository
from infrastructure.localization.json_localization import JSONLocalizationAdapter

from application.use_cases.user_service import UserService
from application.use_cases.agent_service import AgentService
from application.use_cases.vehicle_service import VehicleService
from application.use_cases.violation_service import ViolationService
from application.use_cases.auth_service import AuthService

from domain.models.user import User
from domain.models.vehicle import Vehicle
from domain.models.agent import Agent
from domain.models.violation import Violation
from domain.models.auth import Auth


@pytest.fixture(scope="function")
def mongo_db():
    connect(
        "mongoenginetest",
        host="localhost",
        alias="default",
        mongo_client_class=mongomock.MongoClient,
        uuidRepresentation="standard",
    )
    yield
    disconnect()


@pytest.fixture(scope="function")
def localization_adapter():
    return JSONLocalizationAdapter("en")


@pytest.fixture(scope="function")
def user_repository():
    return MongoUserRepository()


@pytest.fixture
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
def user_service(user_repository):
    return UserService(user_repository)


@pytest.fixture(scope="function")
def agent_service(agent_repository):
    return AgentService(agent_repository)


@pytest.fixture(scope="function")
def vehicle_service(vehicle_repository, user_service, localization_adapter):
    return VehicleService(vehicle_repository, user_service, localization_adapter)


@pytest.fixture(scope="function")
def violation_service(violation_repository, vehicle_service):
    return ViolationService(violation_repository, vehicle_service)


@pytest.fixture(scope="function")
def auth_service(auth_repository):
    return AuthService(auth_repository)


@pytest.fixture(scope="function")
def exists_agent(model_agent, agent_repository):
    agent = agent_repository.add_agent(model_agent)
    return agent


@pytest.fixture(scope="function")
def exist_auth_agent(model_auth_agent, auth_repository):
    auth = auth_repository.add_auth(model_auth_agent)
    return auth


@pytest.fixture(scope="function")
def exist_auth_user(model_auth_user, auth_repository):
    auth = auth_repository.add_auth(model_auth_user)
    return auth


@pytest.fixture(scope="function")
def model_auth_agent(exists_agent):
    return Auth(
        username="test", password="1aw434ds.adq", user_id="", agent_id=str(exists_agent.id)
    )


@pytest.fixture(scope="function")
def model_auth_user(exists_user):
    return Auth(
        username="test", password="1aw434ds.adq", user_id=exists_user.id, agent_id=""
    )


@pytest.fixture(scope="function")
def model_user():
    return User(name="John Doe", email="john.doe@example.com")


@pytest.fixture(scope="function")
def model_user_2():
    return User(name="Jay zee", email="test@tes.com")


@pytest.fixture(scope="function")
def model_agent():
    return Agent(name="John Doe", identifier="123456")


@pytest.fixture(scope="function")
def model_violation(exists_agent, exists_vehicle):
    return Violation(
        vehicle=exists_vehicle,
        timestamp=datetime.now(),
        comments="Speeding",
    )


@pytest.fixture(scope="function")
def model_violation_2(exists_agent, exists_vehicle):
    return Violation(
        vehicle=exists_vehicle,
        timestamp=datetime.now(),
        comments="Running a red light",
    )


@pytest.fixture(scope="function")
def exists_user(model_user, user_repository):
    return user_repository.add_user(model_user)


@pytest.fixture(scope="function")
def exists_user_2(model_user_2, user_repository):
    return user_repository.add_user(model_user_2)


@pytest.fixture(scope="function")
def model_vehicle(exists_user):
    return Vehicle(
        license_plate="ABC123", brand="Toyota", color="Red", owner=exists_user
    )


@pytest.fixture(scope="function")
def exists_vehicle(model_vehicle, vehicle_repository):
    return vehicle_repository.add_vehicle(model_vehicle)


@pytest.fixture(scope="function")
def exist_violation(model_violation, violation_repository):
    return violation_repository.add_violation(model_violation)


@pytest.fixture(scope="function")
def exist_violation_2(model_violation_2, violation_repository):
    return violation_repository.add_violation(model_violation_2)
