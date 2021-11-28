from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import config_by_name
from flask_bcrypt import Bcrypt
from flask_cors import CORS

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
ma = Marshmallow()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config["SQLALCHEMY_ECHO"] = True
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    flask_bcrypt.init_app(app)
    return app
