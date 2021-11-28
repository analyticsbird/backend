from flask import jsonify
from werkzeug.exceptions import HTTPException, InternalServerError

def error_handling_service(app):
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        response = jsonify({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        return response, e.code

    @app.errorhandler(InternalServerError)
    def internal_server_error(e):
        response = jsonify({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        return response, e.code
