from abc import ABC, abstractmethod


class IAuthRepository(ABC):
    @abstractmethod
    def add_auth(self, username, password, agent_id, user_id):
        pass

    @abstractmethod
    def get_auth(self, agent_id, user_id):
        pass

    @abstractmethod
    def delete_auth(self, agent_id, user_id):
        pass
