from abc import ABC, abstractmethod


class IViolationRepository(ABC):
    @abstractmethod
    def add_violation(self, violation):
        pass

    @abstractmethod
    def get_violations_by_license_plate(self, license_plate):
        pass
    
    @abstractmethod
    def get_violations(self):
        pass
    
    @abstractmethod
    def get_violations_by_user_email(self, email):
        pass
