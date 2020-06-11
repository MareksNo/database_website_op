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


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


def sitemap():
    links = []
    for rule in application.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = flask.url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return links


@application.context_processor
def inject_endpoints():
    return dict(endpoints=sitemap())


application.run()



'''
To do:

Somehow split context_processor, sitemap and cli commands in seperate Files.
Get requirements of a request

 Add a random object using a decimal value, if error - SQLAlchemy doesnt allow decimal in integer fields, else, forms does something wierd.
 FIX MIGRATIONS, maybe figure out how to move create_database away
 
 So many things to do. Get to work me lol.
'''