from domain.models.base import Base
from domain.models.user import User


class Vehicle(Base):
    def __init__(self, license_plate, brand, color, owner, id=None, updated_at=None):
        super().__init__(id, updated_at)
        self.license_plate = license_plate
        self.brand = brand
        self.color = color
        self.owner = owner

    @property
    def owner(self):
        if self._owner is None:
            return None
        return self._owner

    @owner.setter
    def owner(self, owner):

        if isinstance(owner, User) or isinstance(owner, dict):
            if type(owner) == dict:
                owner = User(**owner)
        else:
            raise ValueError("Owner must be an instance of User or dict.")
        self._owner = owner

    def to_dict(self):
        return {
            "license_plate": self.license_plate,
            "brand": self.brand,
            "color": self.color,
            "owner": self.owner.to_dict() if self.owner else None,
            "id": self.id,
            "updated_at": str(self.updated_at),
        }
