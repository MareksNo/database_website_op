from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ProductSearchForm(FlaskForm):
    search_name = StringField('Search Product', validators=[DataRequired()])
