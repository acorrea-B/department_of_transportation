from mongoengine import StringField, IntField
from infrastructure.db_adapter.mongo.base import Base


class Auth(Base):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    user_id = StringField(default="", nullable=True)
    agent_id = StringField(default="", nullable=True)