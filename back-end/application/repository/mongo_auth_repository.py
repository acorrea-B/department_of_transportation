from application.ports.i_auth_repository import IAuthRepository
from domain.models.auth import Auth
from infrastructure.db_adapter.mongo.aut import Auth as MongoAgent
from shared.utils.logger import logger_error
from mongoengine.errors import NotUniqueError, DoesNotExist
from shared.utils.exceptions import UniqueViolation, NotFoundModel


class MongoAgentRepository(IAgentRepository):
    """
    Repository class for managing agents in MongoDB.
    """

    def add_agent(self, agent):
        """
        Adds a new agent to the repository.

        Args:
            agent (Agent): The agent object to be added.

        Returns:
            Agent: The added agent object.

        Raises:
            UniqueViolation: If an agent with the same identifier already exists.
        """
        try:
            mongo_agent = MongoAgent(name=agent.name, identifier=agent.identifier)
            mongo_agent.save()
        except NotUniqueError as e:
            raise UniqueViolation("agent_exists")

        return Agent(**mongo_agent.to_dict())

    def get_agent_by_identifier(self, identifier):
        """
        Retrieves an agent from the repository based on its identifier.

        Args:
            identifier (str): The identifier of the agent.

        Returns:
            Agent: The retrieved agent object.

        Raises:
            NotFoundModel: If the agent with the specified identifier is not found.
        """
        try:
            mongo_agent = MongoAgent.objects.get(identifier=identifier)
            return Agent(**mongo_agent.to_dict())
        except DoesNotExist:
            raise NotFoundModel("agent_not_found")

    def update_agent(self, agent):
        """
        Updates an existing agent in the repository.

        Args:
            agent (Agent): The updated agent object.

        Returns:
            Agent: The updated agent object.

        Raises:
            NotFoundModel: If the agent with the specified identifier is not found.
        """
        try:
            mongo_agent = MongoAgent.objects.get(identifier=agent.identifier)
        except DoesNotExist:
            raise NotFoundModel("agent_not_found")
        mongo_agent.name = agent.name
        mongo_agent.save()
        return Agent(**mongo_agent.to_dict())

    def delete_agent(self, identifier):
        """
        Deletes an agent from the repository based on its identifier.

        Args:
            identifier (str): The identifier of the agent to be deleted.

        Raises:
            NotFoundModel: If the agent with the specified identifier is not found.
        """
        try:
            agent = MongoAgent.objects.get(identifier=identifier)
            agent.delete()
        except DoesNotExist as e:
            raise NotFoundModel("agent_not_found")

    def get_agents(self):
        """
        Retrieves all agents from the repository.

        Returns:
            list[Agent]: A list of all agent objects in the repository.
        """
        return [Agent(**item.to_dict()) for item in MongoAgent.objects().all()]
