from application.ports.i_user_repository import IUserRepository
from infrastructure.db_adapter.mongo.user import User as MongoUser
from domain.models.user import User
from shared.utils.logger import logger_error


class MongoUserRepository(IUserRepository):
    """
    A repository class for managing user data in a MongoDB database.

    This class provides methods for adding, retrieving, updating, and deleting user objects in the database.

    Attributes:
        None

    Methods:
        add_user(user): Adds a user to the database.
        get_user_by_email(email): Retrieves a user from the database based on their email.
        get_users(): Retrieves all users from the database.
        update_user(user): Updates a user in the database.
        delete_user(email): Deletes a user from the database.

    """

    def add_user(self, user):
        """
        Adds a user to the database.

        Args:
            user (User): The user object to be added.

        Returns:
            User: The added user object.

        Raises:
            Exception: If there is an error adding the user to the database.
        """
        try:
            mongo_user = MongoUser(name=user.name, email=user.email)
            mongo_user.save()
        except Exception as e:
            logger_error(f"Error adding user to database: {str(e)}")
            return None
        return User(name=mongo_user.name, email=mongo_user.email)

    def get_user_by_email(self, email):
        """
        Retrieves a user from the database based on their email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            User: The retrieved user object if found, None otherwise.
        """
        mongo_user = MongoUser.objects(email=email).first()
        if mongo_user:
            return User(name=mongo_user.name, email=mongo_user.email)
        return None

    def get_users(self):
        """
        Retrieves all users from the database.

        Returns:
            list: A list of User objects representing all users in the database.
        """
        return [User(**item.to_dict()) for item in MongoUser.objects().all()]

    def update_user(self, user):
        """
        Updates a user in the database.

        Args:
            user (User): The user object to be updated.

        Returns:
            User: The updated user object.

        """
        mongo_user = MongoUser.objects(email=user.email).first()
        mongo_user.name = user.name
        mongo_user.save()

        return User(name=mongo_user.name, email=mongo_user.email)

    def delete_user(self, email):
        """
        Deletes a user from the database.

        Args:
            email (str): The email of the user to delete.

        Returns:
            None
        """
        try:
            mongo_user = MongoUser.objects(email=email).first()
            mongo_user.delete()
        except Exception as e:
            logger_error(f"Error deleting user from database: {str(e)}")
        finally:
            return None
