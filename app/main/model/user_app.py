from app.main import db


class UserApp(db.Model):
    __tablename__ = "user_app"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    app_id = db.Column(db.Integer, db.ForeignKey("app.id"), nullable=False)
    user_role_id = db.Column(db.Integer, db.ForeignKey("user_role.id"), nullable=False)

    __table_args__ = (db.UniqueConstraint(user_id, app_id, user_role_id),)

    user = db.relationship("User", back_populates="user_app")
    app = db.relationship("App")
    user_role = db.relationship("UserRole", back_populates="user_app")