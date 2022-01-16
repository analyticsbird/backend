from app.main.model.customer_rating import CustomerRating
from marshmallow import fields
from app.main import ma


class CustomerFeedbackSchema(ma.Schema):
    email = fields.String(attribute="email")
    feedback = fields.String(attribute="feedback")
    updatedAt = fields.String(attribute="updated_at")
    class Meta:
        model = CustomerRating


