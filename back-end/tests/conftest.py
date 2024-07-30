import pytest
import mongomock
from datetime import datetime
from mongoengine import connect, disconnect

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
def model_auth_agent(exists_agent):
    return Auth(
        username="test",
        password="1aw434ds.adq",
        user_id="",
        agent_id=str(exists_agent.id),
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
    timestamp=datetime.now()
    return Violation(
        vehicle=exists_vehicle,
        timestamp=timestamp,
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
def model_vehicle(exists_user):
    return Vehicle(
        license_plate="ABC123", brand="Toyota", color="Red", owner=exists_user
    )
