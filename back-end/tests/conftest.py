import pytest
import mongomock
from mongoengine import connect, disconnect
from application.repository.mongo_user_repository import MongoUserRepository


@pytest.fixture(scope="function")
def mongo_db():
    connect(
        "mongoenginetest",
        host="localhost",
        alias="default",
        mongo_client_class=mongomock.MongoClient,
        uuidRepresentation='standard'
    )
    yield
    disconnect()

@pytest.fixture(scope='function')
def user_repository():
    return MongoUserRepository()