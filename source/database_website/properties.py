from flask import Blueprint

from database_website.extensions.database import db

blueprint = Blueprint(
    name='properties',
    import_name=__name__,
)


navigation_bar = {
    'Home': {'url': '//', 'endpoint': 'core.home_page', 'type': 0},
    'Login': {'url': '/login/', 'endpoint': 'users.login', 'type': 1},
    'Register': {'url': '/registration/', 'endpoint': 'users.register', 'type': 1},
    'Add Product': {'url': '/add_product/', 'endpoint': 'products.add_product', 'type': 2},
    'Logout': {'url': '/logout/', 'endpoint': 'users.logout', 'type': 2},
}

# 0 - Show always, 1 - No Login Only, 2- Login Only


@blueprint.app_context_processor
def inject_navigation():
    return dict(nav_bar=navigation_bar)
