from domain.models.base import Base


class Agent(Base):
    def __init__(self, name, identifier, id=None, updated_at=None):
        super().__init__(id, updated_at)
        self.name = name
        self.identifier = identifier

    def to_dict(self):
        return {
            "name": self.name,
            "identifier": self.identifier,
            "id": self.id,
            "updated_at": str(self.updated_at),
        }
