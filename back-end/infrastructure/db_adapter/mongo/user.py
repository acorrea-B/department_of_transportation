from re import match
from mongoengine import StringField
from infrastructure.db_adapter.mongo.base import Base
from shared.utils.exceptions import DataValidationError

class User(Base):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)

    def clean(self):
        if not match(
            r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$", self.email
        ):
            raise DataValidationError("invalid_email")
