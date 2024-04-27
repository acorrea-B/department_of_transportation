from abc import ABC, abstractmethod


class IVehicleRepository(ABC):
    @abstractmethod
    def add_vehicle(self, vehicle):
        pass

    @abstractmethod
    def get_vehicle_by_license_plate(self, license_plate):
        pass

    @abstractmethod
    def update_vehicle(self, vehicle):
        pass

    @abstractmethod
    def delete_vehicle(self, license_plate):
        pass
