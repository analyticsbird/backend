
from typing import Dict, Tuple
from app.main.model import User
from app.main.services.app_service import App
from app.main import db


class Auth:
    @staticmethod
    def register_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            user = User.query.filter_by(email=data.get("email")).first()

            if(user == None):
                new_user = User(email= data.get("email"), password = data.get("password"), full_name =  data.get("full_name"))
                db.session.add(new_user)
                db.session.commit()

                user = User.query.filter_by(email=data.get("email")).first()
                apps = App.get_user_app(user.id)
                auth_token = User.encode_auth_token(user.id, apps)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'user registraion successful',
                        'Authorization': auth_token
                    }
                    return response_object, 200
            else :
                response_object = {
                    'status': 'fail',
                    'message': 'Account already exists'
                }
                return response_object, 401
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                apps = App.get_user_app(user.id)
                auth_token = User.encode_auth_token(user.id, apps)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'created_at': str(user.created_at)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401