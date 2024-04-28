from mongoengine import StringField, IntField
from infrastructure.db_adapter.mongo.base import Base


class Agent(Base):
    name = StringField(required=True)
    identifier = StringField(required=True, unique=True)
