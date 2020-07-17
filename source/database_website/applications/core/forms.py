from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

from database_website.applications.products.models import Product
from database_website.exceptions import CoreException


class ProductSearchForm(FlaskForm):
    search_name = StringField('Search Product', validators=[DataRequired()])
    search_type = SelectField('Select a Category',
                              choices=[('seller', 'Seller'), ('product_name', 'Product name'), ('id', 'Product Id')],
                              validators=[DataRequired()])

    def get_results(self, search_name, search_type, page):
        if search_type == 'seller':
            return Product.query.filter(Product.seller_username.contains(search_name)).paginate(page, 20, False)
        elif search_type == 'product_name':
            return Product.query.filter(Product.product_name.contains(search_name)).paginate(page, 20, False)
        elif search_type == 'id':
            return Product.query.filter(Product.id_product == search_name).paginate(page, 20, False)
        else:
            return CoreException('Invalid Input Selected')
