from datetime import datetime
from domain.models.base import Base
from domain.models.vehicle import Vehicle


class Violation(Base):
    def __init__(self, vehicle, timestamp, comments, id=None, updated_at=None):
        super().__init__(id, updated_at)
        self.vehicle = vehicle
        self.timestamp = timestamp
        self.comments = comments

    @property
    def vehicle(self):
        if self._vehicle is None:
            return None
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):

        if isinstance(vehicle, Vehicle) or isinstance(vehicle, dict):
            if type(vehicle) == dict:
                vehicle = Vehicle(**vehicle)
        else:
            raise ValueError("Owner must be an instance of Vehicle or dict.")
        self._vehicle = vehicle

    @property
    def timestamp(self):
        if self._raw_date is None:
            return None
        return self._raw_date.strftime("%Y-%m-%d %H:%M:%S")

    @timestamp.setter
    def timestamp(self, value):
        if isinstance(value, datetime) or value is None:
            self._raw_date = value

    def to_dict(self):
        return {
            "vehicle": self.vehicle.to_dict() if self.vehicle else None,
            "timestamp": str(self.timestamp),
            "comments": self.comments,
            "id": self.id,
            "updated_at": str(self.updated_at),
        }
