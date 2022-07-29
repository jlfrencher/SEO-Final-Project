from flask_sqlalchemy import SQLAlchemy
from flask_behind_proxy import FlaskBehindProxy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
proxy = FlaskBehindProxy()