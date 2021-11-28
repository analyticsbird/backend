
import datetime
from app.main import db


class App(db.Model):
    """App model for creating apps"""
    __tablename__ = "app"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    # user role realtionship
    # addresses = db.relationship('UserRole', backref='user', lazy=True)
    # app = db.relationship('user', secondary='user_app', backref=db.backref('app'))

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

