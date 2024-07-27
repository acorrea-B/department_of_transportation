from domain.models.base import Base


class Auth(Base):
    def __init__(
        self, username, password, id=None, agent_id=None, user_id=None, updated_at=None
    ):
        super().__init__(id, updated_at)
        self.username = username
        self.password = password
        self.agent_id = agent_id
        self.user_id = user_id

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "agent_id": self.agent_id,
            "user_id": self.user_id,
            "id": str(self.id),
            "updated_at": str(self.updated_at),
        }
