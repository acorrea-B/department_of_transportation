from abc import ABC, abstractmethod


class IViolationRepository(ABC):
    @abstractmethod
    def add_violation(self, violation):
        pass

    @abstractmethod
    def get_violations_by_vehicle(self, vehicle_id):
        pass

    @abstractmethod
    def get_all_violations(self):
        pass

    @abstractmethod
    def get_violation_by_id(self, violation_id):
        pass

    @abstractmethod
    def update_violation(self, violation):
        pass

    @abstractmethod
    def delete_violation(self, violation):
        pass
