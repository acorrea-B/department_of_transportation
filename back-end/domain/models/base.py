from datetime import datetime


class Base:

    def __init__(self, id=None, updated_at=None) -> None:
        self.id = id
        self.updated_at = updated_at

    @property
    def updated_at(self):
        if self._raw_date is None:
            return None
        return self._raw_date.strftime("%Y-%m-%d %H:%M:%S")

    @updated_at.setter
    def updated_at(self, value):
        if isinstance(value, datetime) or value is None:
            self._raw_date = value

    def to_dict(self):
        raise NotImplementedError("You must implement the to_dict method in your class")
