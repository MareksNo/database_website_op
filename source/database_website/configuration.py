import pathlib

SECRET_KEY = 'asdlkasdlkajsd'
SQLALCHEMY_TRACK_MODIFICATIONS = False

ROOT_DIRECTORY = pathlib.Path(__file__).parent.parent.parent

SQLALCHEMY_DATABASE_URI = f'sqlite:///{ROOT_DIRECTORY}/instaclone.db'
