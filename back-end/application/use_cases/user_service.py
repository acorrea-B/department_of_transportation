# application/use_cases/user_service.py

from application.ports.i_user_repository import IUserRepository
from domain.models.user import User

class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def register_user(self, name, email):
        new_user = User(name=name, email=email)
        self.user_repository.add_user(new_user)
        return new_user

    def find_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)
