from application.ports.i_user_repository import IUserRepository
from domain.models.user import User


class UserService:
    def __init__(self, user_repository: IUserRepository):
        """
        Initializes a new instance of the UserService class.

        Args:
            user_repository (IUserRepository): The user repository to be used by the service.
        """
        self.user_repository = user_repository

    def register_user(self, name, email):
        """
        Registers a new user with the given name and email.

        Args:
            name (str): The name of the user.
            email (str): The email address of the user.

        Returns:
            User: The newly registered user object.
        """
        new_user = User(name=name, email=email)
        return self.user_repository.add_user(new_user)

    def find_user_by_email(self, email):
        """
        Find a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            User: The user object if found, None otherwise.
        """
        return self.user_repository.get_user_by_email(email)

    def find_all_users(self):
        """
        Retrieves all users from the user repository.

        Returns:
            list: A list of user objects.
        """
        return self.user_repository.get_users()

    def update_user(self, name, email):
        """
        Updates the information of an existing user.

        Args:
            user (User): The user object to be updated.

        Returns:
            User: The updated user object.
        """
        update_user = User(name=name, email=email)
        return self.user_repository.update_user(update_user)

    def delete_user(self, email):
        """
        Deletes a user by their email address.

        Args:
            email (str): The email address of the user to be deleted.
        """
        return self.user_repository.delete_user(email)
