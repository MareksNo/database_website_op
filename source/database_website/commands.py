from database_website.application import application
from database_website.extensions.database import db


@application.cli.command()
def create_database():
    db.create_all()
