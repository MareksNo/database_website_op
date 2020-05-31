from werkzeug.security import generate_password_hash
from flask_login import UserMixin

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#from config import db, login_manager, app

from database_website.extensions.database import db

#migrate = Migrate(app, db)

#manager = Manager(app)
#manager.add_command('db', MigrateCommand)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    products = db.relationship('Product', backref='seller', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    __table_args__ = {'extend_existing': True}

    def create_password(self, password):
        self.password = generate_password_hash(password=password)

    @classmethod
    def create(cls, email, password, username):

        instance = cls(
            username=username,
            email=email,
        )

        instance.create_password(password=password)

        return instance