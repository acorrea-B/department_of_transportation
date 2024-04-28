from application.ports.i_agent_repository import IAgentRepository
from domain.models.agent import Agent
from infrastructure.db_adapter.mongo.agent import Agent as MongoAgent
from shared.utils.logger import logger_error


class MongoAgentRepository(IAgentRepository):
    """
    Repository class for managing agents in MongoDB.
    """

    def add_agent(self, agent):
        """
        Adds an agent to the MongoDB collection.

        Args:
            agent (Agent): The agent object to be added.
        """
        try:
            mongo_agent = MongoAgent(name=agent.name, identifier=agent.identifier)
            mongo_agent.save()
        except Exception as e:
            logger_error(f"Error adding agent to database: {str(e)}")
            return None
        return Agent(**mongo_agent.to_dict())

    def get_agent_by_identifier(self, identifier):
        """
        Retrieves an agent from the MongoDB collection based on the identifier.

        Args:
            identifier (str): The identifier of the agent.

        Returns:
            Agent: The agent object if found, None otherwise.
        """
        mongo_agent = MongoAgent.objects(identifier=identifier).first()
        if mongo_agent:
            return Agent(**mongo_agent.to_dict())
        return None

    def update_agent(self, agent):
        """
        Updates an agent in the MongoDB collection.

        Args:
            agent (Agent): The updated agent object.
        """
        mongo_agent = MongoAgent.objects.get(identifier=agent.identifier)
        if not mongo_agent:
            return None
        mongo_agent.name = agent.name
        mongo_agent.save()
        return Agent(**mongo_agent.to_dict())

    def delete_agent(self, identifier):
        """
        Deletes an agent from the MongoDB collection based on the identifier.

        Args:
            identifier (str): The identifier of the agent.
        """
        try:
            MongoAgent.objects(identifier=identifier).delete()
        except Exception as e:
            logger_error(f"Error deleting agent from database: {str(e)}")
            return None

    def get_agents(self):
        return [Agent(**item.to_dict()) for item in MongoAgent.objects().all()]
