from application.ports.i_user_repository import IUserRepository
from infrastructure.db_adapter.mongo.user import User as MongoUser
from domain.models.user import User
from shared.utils.logger import logger_error


class MongoUserRepository(IUserRepository):
    def add_user(self, user):
        try:
            mongo_user = MongoUser(name=user.name, email=user.email)
            mongo_user.save()
        except Exception as e:
            logger_error(f"Error adding user to database: {str(e)}")
            return None
        return User(name=mongo_user.name, email=mongo_user.email)

    def get_user_by_email(self, email):
        mongo_user = MongoUser.objects(email=email).first()
        if mongo_user:
            return User(name=mongo_user.name, email=mongo_user.email)
        return None

    def get_users(self):
        return MongoUser.objects().all()

    def update_user(self, user):
        mongo_user = MongoUser.objects(email=user.email).first()
        mongo_user.name = user.name
        mongo_user.save()

        return User(name=mongo_user.name, email=mongo_user.email)

    def delete_user(self, email):
        try:
            mongo_user = MongoUser.objects(email=email).first()
            mongo_user.delete()
        except Exception as e:
            logger_error(f"Error delete user to database: {str(e)}")
        finally:
            return None
