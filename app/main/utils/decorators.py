from functools import wraps
from typing import Callable
from flask import request

from app.main.services.auth_service import Auth
from app.main.model import User


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated

def has_app_access(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        # get the auth token
        auth_token = request.headers.get('Authorization')
        token_data = User.auth_token_data(auth_token)
        
        apps = token_data['apps']['user_app']

        post_data = request.json
        app_id = post_data.get('app_id')

        if not any(app['app_id'] == app_id for app in apps):
            return {"status":"fail", "message":"Not authorised"}, 401
        
        return f(*args, **kwargs)
    return decorated