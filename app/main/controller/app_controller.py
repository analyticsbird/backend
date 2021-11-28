from flask import  Blueprint, request
from flask_expects_json import expects_json

from app.main.utils.validation_schema import app_schema
from app.main.utils.decorators import token_required
from app.main.services.app_service import App
from app.main.model import User

""" create a app for a user """
api = Blueprint("app", __name__)


@api.route('', methods = ['POST'])
@token_required
@expects_json(app_schema)
def create_app():
    return App.create_app()
    

@api.route('/', methods = ['GET'])
@token_required
def get_all_app():
    auth_token = request.headers.get('Authorization')
    user_id = User.decode_auth_token(auth_token)
    apps = App.get_user_app(user_id)
    return { "status":"success","data": apps }, 200
