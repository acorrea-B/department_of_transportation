from re import match
from mongoengine import StringField, ValidationError
from infrastructure.db_adapter.mongo.base import Base


class User(Base):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)

    def clean(self):
        if not match(
            r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$", self.email
        ):
            raise ValidationError("Invalid email format")
