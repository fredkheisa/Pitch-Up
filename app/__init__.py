from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

     # Creating the app configurations
    app.config.from_object(config_options[config_name])

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # Initializing flask extensions
    db.init_app(app)

    return app