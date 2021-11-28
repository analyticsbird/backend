
import pandas as pd

from typing import Dict, Tuple
from app.main import db
from flask import request
from app.main.utils.app_id_generator import generate_app_id
from app.main.model import User, App as AppModel, UserRole, UserApp
from app.main.serializers.app_schema import UserSchema


class App:
    @staticmethod
    def create_app() -> Tuple[Dict[str, str], int]:
        auth_token = request.headers.get('Authorization')
        user_id = User.decode_auth_token(auth_token)

        user = User.query.filter_by(id= user_id).first()
        user_role = UserRole.query.filter_by(role="ADMIN").first()
        
        if user_role != None:
            data = request.json
            app_id = generate_app_id(13)
            new_app = AppModel(app_id = app_id, name =  data.get("name"))
            db.session.add(new_app)
            db.session.commit()

            app = AppModel.query.filter_by(app_id= app_id).first()
            assoc = UserApp(user= user, app= app ,user_role = user_role)

            db.session.add(assoc)
            db.session.commit()

            return { "status":"success","data":[{"app_id" : app_id}]}, 200

        else:
            return { "status":"fail", "message":"Role not found in user table", "code": 500 }, 500

    @staticmethod
    def get_user_app(user_id: int):
        user_app_obj = User.query.filter(User.user_app.any(id=user_id)).first()
        user_data = {}
        if(user_app_obj):
            user_schema = UserSchema()
            user_data =  user_schema.dump(user_app_obj)
            user_data['user_app'] = (pd.DataFrame(user_data['user_app'])
                .groupby(['app_id','name'])
                .role
                .agg(list)
                .reset_index()
                .to_dict('r'))
            return user_data
        
        else:
            user_data['user_app'] = []
            return user_data