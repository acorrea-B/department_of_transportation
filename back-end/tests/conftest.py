import pytest
import mongomock
from mongoengine import connect, disconnect
from application.repository.mongo_user_repository import MongoUserRepository
from application.repository.mongo_agent_repository import MongoAgentRepository
from application.repository.mongo_vehicle_repository import MongoVehicleRepository

from application.use_cases.user_service import UserService

from domain.models.user import User
from domain.models.vehicle import Vehicle


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
def user_repository():
    return MongoUserRepository()


@pytest.fixture
def agent_repository():
    return MongoAgentRepository()


@pytest.fixture(scope="function")
def vehicle_repository():
    return MongoVehicleRepository()


@pytest.fixture(scope="function")
def model_user():
    return User(name="John Doe", email="john.doe@example.com")


@pytest.fixture(scope="function")
def user_service(user_repository):
    return UserService(user_repository)


@pytest.fixture(scope="function")
def exists_user(model_user, user_repository):

    return user_repository.add_user(model_user)


@pytest.fixture(scope="function")
def model_vehicle(exists_user):
    return Vehicle(
        license_plate="ABC123", brand="Toyota", color="Red", owner=exists_user
    )


@pytest.fixture(scope="function")
def exists_vehicle(model_vehicle, vehicle_repository):
    return vehicle_repository.add_vehicle(model_vehicle)
