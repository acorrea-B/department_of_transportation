from application.ports.i_auth_repository import IAuthRepository
from domain.models.auth import Auth
from infrastructure.db_adapter.mongo.auth import Auth as MongoAuth
from shared.utils.logger import logger_error
from mongoengine.errors import NotUniqueError, DoesNotExist
from shared.utils.exceptions import UniqueViolation, NotFoundModel


class MongoAuthRepository(IAuthRepository):
    """
    Repository class for managing auth in MongoDB.
    """

    def add_auth(self, auth):
        """
        Adds a new auth to the repository.

        Args:
            auth (Auth): The auth object to be added.

        Returns:
            Auth: The added Auth object.

        Raises:
            UniqueViolation: If an auth with the same username already exists.
        """
        try:
            mongo_auth = MongoAuth(username=auth.username, password=auth.password, user_id=auth.user_id, agent_id=auth.agent_id)
            mongo_auth.save()
        except NotUniqueError as e:
            raise UniqueViolation("auth_exists")

        return Auth(**mongo_auth.to_dict())

    def get_auth(self, username, password):
        """
        Retrieves an auth from the repository based on its username.

        Args:
            username (str): The username of the auth.
            password (str): The password of the auth.

        Returns:
            auth: The retrieved auth object.

        Raises:
            NotFoundModel: If the auth with the specified username is not found.
        """
        try:
            mongo_auth = MongoAuth.objects.get(username=username, password=password)
            return Auth(**mongo_auth.to_dict())
        except DoesNotExist:
            raise NotFoundModel("auth_not_found")

    def delete_auth(self, username):
        """
        Deletes an auth from the repository based on its username.

        Args:
            username (str): The username of the auth to be deleted.

        Raises:
            NotFoundModel: If the auth with the specified username is not found.
        """
        try:
            mongo_auth = MongoAuth.objects.get(username=username)
            mongo_auth.delete()
        except DoesNotExist as e:
            raise NotFoundModel("auth_not_found")
