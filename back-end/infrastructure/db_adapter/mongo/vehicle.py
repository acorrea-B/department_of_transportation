from mongoengine import StringField, ReferenceField
from infrastructure.db_adapter.mongo.base import Base
from infrastructure.db_adapter.mongo.user import User


class Vehicle(Base):
    license_plate = StringField(required=True, unique=True)
    brand = StringField(required=True)
    color = StringField(required=True)
    owner = ReferenceField(User, reverse_delete_rule=4)
