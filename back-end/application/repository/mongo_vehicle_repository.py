from mongoengine import DoesNotExist, ValidationError
from application.ports.i_vehicle_repository import IVehicleRepository
from infrastructure.db_adapter.mongo.vehicle import Vehicle as MongoVehicle
from domain.models.vehicle import Vehicle
from shared.utils.logger import logger_error
from bson import ObjectId


class MongoVehicleRepository(IVehicleRepository):
    """
    Repository class for interacting with MongoDB to perform CRUD operations on vehicles.
    """

    def add_vehicle(self, vehicle):
        """
        Adds a new vehicle to the database.

        Args:
            vehicle (Vehicle): The vehicle object to be added.

        Returns:
            Vehicle: The added vehicle object if successful, None otherwise.
        """
        try:
            mongo_vehicle = MongoVehicle(
                license_plate=vehicle.license_plate,
                brand=vehicle.brand,
                color=vehicle.color,
                owner=ObjectId(vehicle.owner.id),
            )
            mongo_vehicle.save()
            return Vehicle(**mongo_vehicle.to_dict())
        except ValidationError as e:
            logger_error(f"Validation Error: {str(e)}")
            return None

    def get_vehicle_by_license_plate(self, license_plate):
        """
        Retrieves a vehicle from the database based on the license plate.

        Args:
            license_plate (str): The license plate of the vehicle.

        Returns:
            Vehicle: The retrieved vehicle object if found, None otherwise.
        """
        try:
            return Vehicle(
                **MongoVehicle.objects.get(license_plate=license_plate).to_dict()
            )
        except DoesNotExist:
            return None

    def update_vehicle(self, vehicle):
        """
        Updates an existing vehicle in the database.

        Args:
            vehicle (Vehicle): The updated vehicle object.

        Returns:
            Vehicle: The updated vehicle object if successful, None otherwise.
        """
        try:
            mongo_vehicle = MongoVehicle.objects.get(license_plate=vehicle.license_plate)
            if mongo_vehicle:
                mongo_vehicle.brand = vehicle.brand
                mongo_vehicle.color = vehicle.color
                mongo_vehicle.owner = ObjectId(vehicle.owner.id)
                mongo_vehicle.save()
                return Vehicle(**mongo_vehicle.to_dict())
        except ValidationError as e:
            logger_error(f"Validation Error: {str(e)}")
            return None

    def delete_vehicle(self, license_plate):
        """
        Deletes a vehicle from the database based on the license plate.

        Args:
            license_plate (str): The license plate of the vehicle to be deleted.

        Returns:
            bool: True if the vehicle was deleted successfully, False otherwise.
        """
        try:
            MongoVehicle.objects.get(license_plate=license_plate).delete()
            return True
        except Exception as e:
            logger_error(f"Error deleting vehicle from database: {str(e)}")
            return False

    def get_all_vehicles(self):
        """
        Retrieves all vehicles from the database.

        Returns:
            list: A list of Vehicle objects representing all the vehicles in the database.
        """
        return [Vehicle(**vehicle.to_dict()) for vehicle in MongoVehicle.objects.all()]
