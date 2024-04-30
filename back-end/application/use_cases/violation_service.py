from application.ports.i_violations_repository import IViolationRepository
from domain.models.violation import Violation
from shared.utils.exceptions import NotFoundModel

class ViolationService:
    def __init__(self, violation_repository: IViolationRepository, vehicle_service):
        """
        Initializes a new instance of the ViolationService class.

        Args:
            violation_repository (IViolationRepository): The repository for violations.
            vehicle_service: The service for managing vehicles.
        """
        self.violation_repository = violation_repository
        self.vehicle_service = vehicle_service

    def register_violation(self, license_plate, comments, timestamp):
        """
        Registers a violation for a vehicle.

        Args:
            license_plate (str): The license plate of the vehicle.
            comments (str): Additional comments about the violation.
            timestamp (datetime): The timestamp of the violation.

        Returns:
            int: The ID of the registered violation.

        """
        vehicle = self.vehicle_service.find_vehicle_by_plate(license_plate)
        if not vehicle:
            raise NotFoundModel("vehicle_not_found")
        violation = Violation(vehicle=vehicle, comments=comments, timestamp=timestamp)
        return self.violation_repository.add_violation(violation)

    def get_violations_by_vehicle(self, license_plate):
        """
        Retrieves all violations associated with a specific vehicle.

        Args:
            license_plate: The license plate of the vehicle.

        Returns:
            A list of violations associated with the vehicle.
        """
        vehicle = self.vehicle_service.find_vehicle_by_plate(license_plate)
        return self.violation_repository.get_violations_by_vehicle(vehicle.id)

    def get_violation(self, violation_id):
        """
        Retrieves a violation by its ID.

        Args:
            violation_id: The ID of the violation.

        Returns:
            The violation with the specified ID.

        Raises:
            NotFoundModel: If the violation is not found.
        """
        return self.violation_repository.get_violation_by_id(violation_id)

    def get_all_violations(self):
        """
        Retrieves all violations.

        Returns:
            A list of all violations.
        """
        return self.violation_repository.get_all_violations()

    def update_violation(self, violation):
        """
        Updates an existing violation.

        Args:
            violation: The violation to be updated.

        Returns:
            The updated violation.
        """
        return self.violation_repository.update_violation(violation)

    def delete_violation(self, violation):
        """
        Deletes a violation.

        Args:
            violation: The violation to be deleted.
        """
        self.violation_repository.delete_violation(violation)