from datetime import datetime
from mongoengine import StringField, ReferenceField, DateTimeField
from infrastructure.db_adapter.mongo.vehicle import Vehicle
from infrastructure.db_adapter.mongo.base import Base


class Violation(Base):
    vehicle = ReferenceField(Vehicle, reverse_delete_rule=4)
    timestamp = DateTimeField(default=datetime.now())
    comments = StringField()
