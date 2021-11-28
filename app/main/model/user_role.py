
from app.main import db
import datetime


class UserRole(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user_role"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(100), nullable=False)

    user_app = db.relationship("UserApp", back_populates="user_role")
    

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

