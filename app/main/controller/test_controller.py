from flask import Flask, Blueprint
from app.main.model import User
from .. import db

api = Blueprint("test", __name__)


@api.route('/')
def hello_world():
    return 'Hello, World!'
