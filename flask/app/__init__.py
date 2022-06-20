from flask import Flask
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
import jwt

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)


app.config["JWT_SECRET_KEY"] = "eduarda17"
jwt = JWTManager(app)



port=app.config["FLASK_PORT"]
host=app.config["FLASK_HOST"]

server = Server(host=host, port=port)
manager.add_command("runserver", server)
manager.add_command("db", MigrateCommand)

from app.models.controller import Controller
from app.models.user import User
from app.models.role import Role
from app.models.action import Action
from app.models.resource import Resource
from app.models.privilege import Privilege

from app.controllers import user
from app.controllers import role
from app.controllers import controller
from app.controllers import privilege
from app.controllers import action
from app.controllers import resource
from app.controllers import auth
