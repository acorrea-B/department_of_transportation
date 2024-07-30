import pytest
import mongomock


from application.use_cases.user_service import UserService
from application.use_cases.agent_service import AgentService
from application.use_cases.vehicle_service import VehicleService
from application.use_cases.violation_service import ViolationService
from application.use_cases.auth_service import AuthService

from tests.repository.mongo.conftest import (
    agent_repository,
    user_repository,
    vehicle_repository,
    localization_adapter,
    auth_repository,
    violation_repository,
    exist_auth_agent,
    exist_auth_user,
    exist_violation,
    exist_violation_2,
    exists_agent,
    exists_user,
    exists_user_2,
    exists_vehicle,
)


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
