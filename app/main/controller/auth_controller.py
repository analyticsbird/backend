from flask import Flask, request, Blueprint
from flask_expects_json import expects_json
from app.main.model import User
from app.main.utils.validation_schema import register_schema, login_schema
from app.main.services.auth_service import Auth


api = Blueprint("auth", __name__)

@api.route('/register', methods = ['POST'])
@expects_json(register_schema)
def register():
    post_data = request.json
    return Auth.register_user(post_data)

@api.route('/login', methods = ['POST'])
@expects_json(login_schema)
def login():
    post_data = request.json
    return Auth.login_user(post_data)

