from mongoengine import StringField
from infrastructure.db_adapter.mongo.base import Base


class User(Base):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)

    