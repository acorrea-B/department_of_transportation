from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def get_user_by_email(self, email):
        pass

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def update_user(self, user):
        pass

    @abstractmethod
    def delete_user(self, email):
        pass
