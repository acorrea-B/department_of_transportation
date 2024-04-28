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
        result = self.reload().to_mongo()
        response = {}
        for key, value in result.items():
            key = key if key != "_id" else "id"
            value = getattr(self, key)
            if isinstance(value, Document):
                response[key] = value.to_dict()
                continue
            response[key] = value

        return response

    def save(self, *args, **kwargs):

        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)
