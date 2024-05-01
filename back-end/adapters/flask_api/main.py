from flask import Flask
from infrastructure.localization.json_localization import JSONLocalizationAdapter
from application.use_cases.user_service import UserService
from application.repository.mongo_user_repository import MongoUserRepository

from adapters.flask_api.routes.user_routes import user_blueprint
from mongoengine import connect


class DependenciContainer:
    def __init__(self):
        connect(
            db="test",
            username="user",
            password="123456",
            host="mongodb://user:123456@localhost/",
        )

    service_user = UserService(MongoUserRepository())
    localization = JSONLocalizationAdapter("en", "shared/localization/")


app = Flask(__name__)

user_blueprint.dependencie_container = DependenciContainer()
app.register_blueprint(user_blueprint)
