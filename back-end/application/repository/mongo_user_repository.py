from application.ports.i_user_repository import IUserRepository
from infrastructure.db_adapter.mongo.user import User
from domain.models.user import User


class MongoUserRepository(IUserRepository):
    def add_user(self, user):
        mongo_user = User(name=user.name, email=user.email)
        mongo_user.save()

    def get_user_by_email(self, email):
        mongo_user = User.objects(email=email).first()
        if mongo_user:
            return User(name=mongo_user.name, email=mongo_user.email)
        return None