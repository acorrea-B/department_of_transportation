from domain.models.base import Base


class Violation(Base):
    def __init__(self, license_plate, timestamp, comments, id=None, updated_at=None):
        super().__init__(id, updated_at)
        self.license_plate = license_plate
        self.timestamp = timestamp
        self.comments = comments

    def to_dict(self):
        return {
            "license_plate": self.license_plate,
            "timestamp": self.timestamp,
            "comments": self.comments,
            "id": self.id,
            "updated_at": str(self.updated_at),
        }
