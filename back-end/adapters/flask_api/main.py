from flask import Flask
from adapters.flask_api.routes.user_routes import user_blueprint
from mongoengine import connect

connect(
    db='test',
    username='user',
    password='123456',
    host='mongodb://user:123456@localhost/'
)

app = Flask(__name__)

app.register_blueprint(user_blueprint)

