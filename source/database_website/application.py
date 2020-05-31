import flask

from database_website.extensions.database import db

class Application(flask.Flask):
    def load_configuration(self):
        self.config.from_pyfile('configuration.py')

    def configure_database(self):
        from database_website.extensions.database import db

        db.init_app(app=self)

    def configure_login_manager(self):
        from database_website.extensions.auth import login_manager

        login_manager.init_app(app=self)

    def register_applications(self):
        from database_website.applications.core.urls import blueprint as core_blueprint
        from database_website.applications.users.urls import blueprint as users_blueprint
        from database_website.applications.products.urls import blueprint as products_blueprint

        self.register_blueprint(blueprint=users_blueprint)
        self.register_blueprint(blueprint=products_blueprint)
        self.register_blueprint(blueprint=core_blueprint)

    @classmethod
    def create(cls):
        instance = Application(__name__)

        instance.load_configuration()
        instance.configure_database()
        instance.configure_login_manager()
        instance.register_applications()

        return instance

application = Application.create()



@application.cli.command()
def create_database():
    db.create_all()

application.run()


# FIX MIGRATIONS, maybe figure out how to move create_database away


# Add a random object using a decimal value, if error - SQLAlchemy doesnt allow decimal in integer fields, else, forms does something wierd.
