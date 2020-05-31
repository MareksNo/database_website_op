from flask_login import current_user, login_required
from flask import Flask, render_template, url_for, flash, redirect, request

from database_website.applications.products import forms
from database_website.applications.products.models import Product
from database_website.applications.views import FormViewMixin


from flask.views import MethodView


class AddProductView(MethodView, FormViewMixin):
    decorators = [
        login_required,
    ]

    form_class = forms.AddProductForm
    template_name = 'products/add_product.html'
    title = 'Add Product'

    def post(self):
        form = self.get_form()

        if form.validate_on_submit():

            product = Product.add_product(product_name=form.product_name.data,
                                          price=form.price.data,
                                          seller_username=current_user.username)

            flash('Added a product successfully!', category='success')
            return redirect(url_for('core.home_page'))

        else:
            flash('Whoops you did big messed up nonono')


class DisplayProductView(MethodView):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return render_template('products/display_product.html', title=product.product_name, product=product)


class SearchProductView(MethodView):
    def get(self, search_name):
        products = Product.query.filter(Product.product_name.contains(search_name))
        return render_template('products/search_product.html', title=search_name, products=products)
