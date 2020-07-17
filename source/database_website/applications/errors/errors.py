import flask

from flask import Blueprint

blueprint = Blueprint(
    name='errors',
    import_name=__name__,
    template_folder='templates',
)


@blueprint.app_errorhandler(404)
def page_not_found(e):
    return flask.render_template('errors/404.html', error=e)


@blueprint.app_errorhandler(401)
def unauthorized(e):
    return flask.render_template('errors/401.html')
