from flask import Blueprint

from database_website.applications.products import views

blueprint = Blueprint(
    name='products',
    import_name=__name__,
    template_folder='templates',
)

blueprint.add_url_rule(
    rule='/add_product/',
    view_func=views.AddProductView.as_view('add_product'),
)

blueprint.add_url_rule(
    rule='/product/<int:product_id>',
    view_func=views.DisplayProductView.as_view('display_product'),
)

blueprint.add_url_rule(
    rule='/product/search/<search_name>',
    view_func=views.SearchProductView.as_view('search_product'),
)
