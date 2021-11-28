from flask import Flask

def create_controllers(app: Flask, controllers: list)-> Flask:
    for controller in controllers:
        app.register_blueprint(controller["name"], url_prefix='/api/v1{}'.format(controller["path"]))

    return app