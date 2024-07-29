from application.ports.i_auth_repository import IAuthRepository
from domain.models.auth import Auth


class AuthService:
    """
    This class represents the service layer for managing agents.
    """

    def __init__(self, auth_repository: IAuthRepository):
        self.auth_repository = auth_repository

    def register_auth(self, username, password, user_id=None, agent_id=None):
        """
        Registers a new auth with the given username and password.

        Args:
            username (str): The username of the auth.
            password (str): The password of the auth.
            user_id  (str): The id unique of user.
            agent_id  (str): The id unique of agent.

        Returns:
            Auth: The registered auth object.
        """
        auth = Auth(username=username, password=password, user_id=user_id, agent_id=agent_id)
        return self.auth_repository.add_auth(auth)

    def remove_auth(self, username):
        """
        Removes an auth by its username.

        Args:
            username (str): The username of the auth to remove.
        """
        return self.auth_repository.delete_auth(username)

    def get_auth(self, username, password):
        """
        Retrieves auth with username and password.

        Returns:
            Auth: The registered auth object
        """
        return self.auth_repository.get_auth(username, password)
