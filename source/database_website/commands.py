from flask import Blueprint

from database_website.extensions.database import db

blueprint = Blueprint(
    name='commands',
    import_name=__name__,
)


@blueprint.cli.command()
def create_database():
    db.create_all()
