from flask import Blueprint

from database_website.applications.core import views

blueprint = Blueprint(
    name='core',
    import_name=__name__,
    template_folder='templates',
)


blueprint.add_url_rule(
    rule='//',
    view_func=views.HomePageView.as_view('home_page'),
)
