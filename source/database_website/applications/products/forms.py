from flask_wtf import FlaskForm
from flask_login import current_user

from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    product_name = StringField('Product Name',
                               validators=[DataRequired()])
    price = IntegerField(validators=[DataRequired()])
    description = StringField('Product description')


class DeleteProductForm(FlaskForm):
    delete = SubmitField('Delete')

# iNTEGER NEEDS TO BE CHANGED TO DECIMAL, requires sqlalchemy to be altered
