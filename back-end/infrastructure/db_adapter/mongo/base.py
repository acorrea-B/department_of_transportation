from mongoengine import Document, DateTimeField
from bson import ObjectId
from datetime import datetime


class Base(Document):
    meta = {
        "abstract": True,
        "strict": False,
    }
    updated_at = DateTimeField(default=datetime.now())

    def to_dict(self):
        result = self.to_mongo().to_dict()
        response = result.copy()
        for key, value in result.items():
            if isinstance(value, ObjectId):
                if key == "_id":
                    response.pop(key)
                    key = "id"
                response[key] = str(value)

        return response

    def save(self, *args, **kwargs):

        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)
