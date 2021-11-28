from app.main import db
import datetime

class CustomerRating(db.Model):
    __tablename__ = "customer_rating"

    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey("app.id"), nullable=False)
    customer_id = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50))
    feedback = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)