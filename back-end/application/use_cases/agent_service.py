from application.ports.i_agent_repository import IAgentRepository
from domain.models.agent import Agent

class AgentService:
    """
    This class represents the service layer for managing agents.
    """

    def __init__(self, agent_repository: IAgentRepository):
        self.agent_repository = agent_repository

    def register_agent(self, name, identifier):
        """
        Registers a new agent with the given name and identifier.

        Args:
            name (str): The name of the agent.
            identifier (str): The identifier of the agent.

        Returns:
            Agent: The registered agent object.
        """
        agent = Agent(name=name, identifier=identifier)
        return self.agent_repository.add_agent(agent)

    def find_agent_by_identifier(self, identifier):
        """
        Finds an agent by its identifier.

        Args:
            identifier (str): The identifier of the agent to find.

        Returns:
            Agent: The found agent object, or None if not found.
        """
        return self.agent_repository.get_agent_by_identifier(identifier)

    def update_agent(self, name, identifier):
        """
        Updates an agent with the given name and identifier.

        Args:
            name (str): The new name of the agent.
            identifier (str): The identifier of the agent to update.
        """
        agent = Agent(name=name, identifier=identifier)
        self.agent_repository.update_agent(agent)

    def remove_agent(self, identifier):
        """
        Removes an agent by its identifier.

        Args:
            identifier (str): The identifier of the agent to remove.
        """
        self.agent_repository.delete_agent(identifier)

    def find_all_agents(self):
            """
            Retrieves all agents from the agent repository.

            Returns:
                A list of all agents.
            """
            return self.agent_repository.get_agents()
