from abc import ABC, abstractmethod


class IAgentRepository(ABC):
    @abstractmethod
    def add_agent(self, violation):
        pass

    @abstractmethod
    def get_agents(self, license_plate):
        pass

    @abstractmethod
    def get_agent_by_id(self, license_plate):
        pass

    @abstractmethod
    def update_agent(self, agent):
        pass

    @abstractmethod
    def delete_agent(self, license_plate):
        pass
