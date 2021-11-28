import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.main import create_app, db
from app.main.controller import controllers
from app.main.utils.create_controllers import create_controllers
from app.main.services.error_handling_service import error_handling_service

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app = create_controllers(app, controllers)
error_handling_service(app)
app.app_context().push()


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(debug=True)

if __name__ == "__main__":
    manager.run()