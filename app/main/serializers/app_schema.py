from app.main.model.app import App
from marshmallow import fields
from app.main import ma


class UserAppSchema(ma.Schema):
    name = fields.String(attribute="app.name")
    app_id = fields.String(attribute="app.app_id")
    role = fields.String(attribute="user_role.role")
    class Meta:
        fields = ('app_id','name', 'role')
        model = App

class UserSchema(ma.Schema):
    user_app = ma.Nested(UserAppSchema, many = True)

