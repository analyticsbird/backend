from flask import Blueprint, request
from app.main.model import CustomerRating, App
from app.main.utils.decorators import token_required, has_app_access
from .. import db

api = Blueprint("rating", __name__)


@api.route('', methods = ['POST'])
def create_and_update_rating():
    post_data = request.json
    app_id = post_data.get('app_id')
    rating = post_data.get('rating')
    customer_id = post_data.get('customer_id')
    app = App.query.filter_by(app_id= app_id).first()
    if app:
        try:
            customer = CustomerRating.query.filter_by(customer_id = customer_id).first()
            if customer:
                customer.rating = rating
                db.session.commit()
                return { "status":"success","message": "updated rating" }, 200
            else:
                new_rating = CustomerRating(app_id = app.id, rating = rating, customer_id = customer_id)
                db.session.add(new_rating)
                db.session.commit()
                return { "status":"success","message": "added rating" }, 200
        except Exception as e:
            return {"status":"fail","message": str(e) }, 404
    else:
        return { "status":"fail","message": "invalid app id" }, 404


@api.route('/feedback', methods = ['PATCH'])
def feedback():
    post_data = request.json
    app_id = post_data.get('app_id')
    customer_id = post_data.get('customer_id')
    email = post_data.get('email')
    feedback = post_data.get('feedback')
    app = App.query.filter_by(app_id= app_id).first()
    try:
        customer = CustomerRating.query.filter_by(customer_id = customer_id, app_id = app.id).first()
        if customer:
            customer.email = email
            customer.feedback = feedback
            db.session.commit()
            return { "status":"success", "message":"feedback added" }, 200
        else:
            return { "status":"fail", "message":"customer does not exist" }, 404
    except Exception as e:
            return {"status":"failure","message": str(e) }


@api.route('/report', methods = ['GET'])
@token_required
@has_app_access
def totalRating():
    app_id = request.args.get("app_id")
    
    if app_id:
        app = App.query.filter_by(app_id= app_id).first()
        customer_ratings = db.session.query(
            CustomerRating.rating, 
            db.func.count(CustomerRating.rating)
        ).filter(CustomerRating.app_id == app.id
        ).group_by(CustomerRating.rating).all()

        total_ratings = db.session.query(
            CustomerRating.rating
        ).filter(CustomerRating.app_id == app.id
        ).count()

        total_feedback = db.session.query(
            CustomerRating.feedback
        ).filter(CustomerRating.app_id == app.id, CustomerRating.feedback.isnot(None)
        ).count()
        
        rating = {
            "1":0,
            "2":0,
            "3":0,
            "4":0,
            "5":0,
        }
        
        for customer in customer_ratings:
            rating[str(customer[0])] = customer[1]

        return {
                "data":{ 
                    "totalRating": total_ratings, 
                    "totalFeedback": total_feedback, 
                    "ratings": rating
                },
                "status":"success"
            }
    else:
        return { "status":"fail", "message":"Invalid app_id" }, 404
