from flask import Flask

from application.use_cases.user_service import UserService
from application.use_cases.agent_service import AgentService
from application.use_cases.vehicle_service import VehicleService

from infrastructure.localization.json_localization import JSONLocalizationAdapter
from application.repository.mongo_user_repository import MongoUserRepository
from application.repository.mongo_agent_repository import MongoAgentRepository
from application.repository.mongo_vehicle_repository import MongoVehicleRepository

from adapters.flask_api.routes.user_routes import user_blueprint
from adapters.flask_api.routes.agent_routes import agent_blueprint
from adapters.flask_api.routes.vehicle_routes import vehicle_blueprint
from mongoengine import connect


class DependenciContainer:
    def __init__(self):
        connect(
            db="test",
            username="user",
            password="123456",
            host="mongodb://user:123456@localhost/",
        )

    localization = JSONLocalizationAdapter("en", "shared/localization/")
    service_user = UserService(MongoUserRepository())
    service_agent = AgentService(MongoAgentRepository())
    vehicle_service = VehicleService(
        MongoVehicleRepository(), service_user, localization
    )


app = Flask(__name__)

user_blueprint.dependencie_container = DependenciContainer()
agent_blueprint.dependencie_container = DependenciContainer()
vehicle_blueprint.dependencie_container = DependenciContainer()

app.register_blueprint(user_blueprint)
app.register_blueprint(agent_blueprint)
app.register_blueprint(vehicle_blueprint)
