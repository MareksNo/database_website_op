from flask import Blueprint
#from config import app

from database_website.applications.users import views

blueprint = Blueprint(
    name='users',
    import_name=__name__,
    template_folder='templates',
)

blueprint.add_url_rule(
    rule='/register/',
    view_func=views.RegistrationView.as_view('register'),
)

blueprint.add_url_rule(
    rule='/login/',
    view_func=views.LoginView.as_view('login'),
)

blueprint.add_url_rule(
    rule='/logout/',
    view_func=views.LogoutView.as_view('logout'),
)
