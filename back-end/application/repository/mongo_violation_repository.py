from application.ports.i_violations_repository import IViolationRepository
from infrastructure.db_adapter.mongo.violation import Violation as MongoViolation
from domain.models.violation import Violation
from shared.utils.logger import logger_error
from bson import ObjectId
from shared.utils.exceptions import DataValidationError, BDInsertError, NotFoundModel
from mongoengine import DoesNotExist


class MongoViolationsRepository(IViolationRepository):

    def add_violation(self, violation):
        """
        Adds a violation to the database.

        Args:
            violation (Violation): The violation object to be added.

        Returns:
            Violation: The added violation object.

        Raises:
            Exception: If there is an error adding the violation to the database.
        """
        try:
            mongo_violation = MongoViolation(
                vehicle=ObjectId(violation.vehicle.id),
                comments=violation.comments,
                timestamp=violation.timestamp,
            )
            mongo_violation.save()
        except DataValidationError as e:
            raise DataValidationError(str(e))
        except Exception as e:
            logger_error(f"Error adding violation to database: {str(e)}")
            raise BDInsertError(str(e))
        return Violation(**mongo_violation.to_dict())

    def get_violations_by_vehicle(self, vehicle_id):
        """
        Retrieves violations associated with a specific vehicle.

        Args:
            vehicle_id (str): The ID of the vehicle.

        Returns:
            list: A list of Violation objects associated with the vehicle.
        """
        violations = MongoViolation.objects.filter(vehicle=ObjectId(vehicle_id))
        return [Violation(**violation.to_dict()) for violation in violations]

    def get_all_violations(self):
        """
        Retrieves all violations from the database.

        Returns:
            list: A list of Violation objects representing all violations in the database.
        """
        return [Violation(**item.to_dict()) for item in MongoViolation.objects().all()]

    def update_violation(self, violation):
        """
        Updates a violation in the database.

        Args:
            violation (Violation): The violation object to be updated.

        Returns:
            Violation: The updated violation object.

        """
        try:
            mongo_violation = MongoViolation.objects.get(id=violation.id)
        except DoesNotExist as e:
            raise NotFoundModel("violation_not_found")

        mongo_violation.comments = violation.comments
        mongo_violation.timestamp = violation.timestamp
        mongo_violation.save()
        return Violation(**mongo_violation.to_dict())

    def get_violation_by_id(self, violation_id):
        """
        Retrieves a violation by its ID.

        Args:
            violation_id (str): The ID of the violation to retrieve.

        Returns:
            Violation: The violation object.

        Raises:
            NotFoundModel: If the violation is not found.
        """
        try:
            mongo_violation = MongoViolation.objects.get(id=violation_id)
            return Violation(**mongo_violation.to_dict())
        except DoesNotExist:
            raise NotFoundModel("violation_not_found")

    def delete_violation(self, violation_id):
        """
        Deletes a violation from the database.

        Args:
            violation_id (str): The ID of the violation to delete.

        Returns:
            None
        """
        try:
            mongo_violation = MongoViolation.objects.get(id=violation_id)
            mongo_violation.delete()
            return None
        except DoesNotExist as e:
            logger_error(f"Error deleting violation from database: {str(e)}")
            raise NotFoundModel("violation_not_found")
