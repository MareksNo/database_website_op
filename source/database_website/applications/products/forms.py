from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    product_name = StringField('Product Name',
                               validators=[DataRequired()])
    price = IntegerField(validators=[DataRequired()])


# iNTEGER NEEDS TO BE CHANGED TO DECIMAL, requires sqlalchemy to be altered
