from application.ports.i_vehicle_repository import IVehicleRepository
from domain.models.vehicle import Vehicle
from shared.utils.exceptions import NotFoundModel


class VehicleService:
    """
    Service class for managing vehicles.
    """

    def __init__(
        self, vehicle_repository: IVehicleRepository, user_service, localization_adapter
    ):
        """
        Initializes a new instance of the VehicleService class.

        Args:
            vehicle_repository (IVehicleRepository): The vehicle repository.
            user_service: The user service.
            localization_adapter: The localization adapter.
        """
        self.vehicle_repository = vehicle_repository
        self.user_service = user_service
        self.localization_adapter = localization_adapter

    def register_vehicle(self, license_plate, brand, color, owner_email):
        """
        Registers a new vehicle.

        Args:
            license_plate (str): The license plate of the vehicle.
            brand (str): The brand of the vehicle.
            color (str): The color of the vehicle.
            owner_email (str): The email of the vehicle owner.

        Returns:
            int: The ID of the newly registered vehicle.
        """
        owner = self.get_owner(owner_email)
        vehicle = Vehicle(
            license_plate=license_plate, brand=brand, color=color, owner=owner
        )
        return self.vehicle_repository.add_vehicle(vehicle)

    def find_vehicle_by_plate(self, license_plate):
        """
        Finds a vehicle by its license plate.

        Args:
            license_plate (str): The license plate of the vehicle.

        Returns:
            Vehicle: The found vehicle, or None if not found.
        """
        return self.vehicle_repository.get_vehicle_by_license_plate(license_plate)

    def update_vehicle_info(self, license_plate, color, owner_email):
        """
        Update the information of a vehicle.

        Args:
            license_plate (str): The license plate of the vehicle.
            color (str): The new color of the vehicle.
            owner_email (str): The email of the new owner of the vehicle.

        Returns:
            bool: True if the vehicle information was successfully updated, False otherwise.

        Raises:
            NotFoundModel: If the vehicle or the owner is not found.
        """

        if vehicle := self.vehicle_repository.get_vehicle_by_license_plate(
            license_plate
        ):
            if owner := self.get_owner(owner_email):
                vehicle.owner = owner
            vehicle.color = color
            return self.vehicle_repository.update_vehicle(vehicle)
        raise NotFoundModel(self.localization_adapter.get_message("vehicle_not_found"))

    def get_owner(self, owner_email):
        if owner_email:
            if owner := self.user_service.find_user_by_email(owner_email):
                return owner
            raise NotFoundModel(self.localization_adapter.get_message("user_not_found"))

    def remove_vehicle(self, license_plate):
        """
        Removes a vehicle.

        Args:
            license_plate (str): The license plate of the vehicle.

        Returns:
            None

        Raises:
            NotFoundModel: If the vehicle is not found.
        """
        if not self.vehicle_repository.delete_vehicle(license_plate):
            raise NotFoundModel(
                self.localization_adapter.get_message("vehicle_not_found")
            )
        return None
