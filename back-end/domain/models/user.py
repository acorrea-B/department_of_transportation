from domain.models.base import Base

class User(Base):
    def __init__(self, name, email, id=None, updated_at=None):
        super().__init__(id, updated_at)
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "id": str(self.id),
            "updated_at": str(self.updated_at),
        }
