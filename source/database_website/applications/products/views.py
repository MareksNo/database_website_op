from flask_login import current_user, login_required
from flask import Flask, render_template, url_for, flash, redirect, request

from database_website.applications.products import forms
from database_website.applications.products.models import Product
from database_website.applications.views import FormViewMixin
import database_website.applications.core.forms as core_forms


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
            return render_template(self.template_name, title=self.title, form=form)

class DisplayProductView(MethodView):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return render_template('products/display_product.html', title=product.product_name, product=product)


class SearchProductView(MethodView):
    def get(self, search_name):
        form = core_forms.ProductSearchForm()

        products_product_name = Product.query.filter(Product.product_name.contains(search_name))
        products_seller_username = Product.query.filter(Product.seller_username.contains(search_name))
        products_matching_ids = Product.query.filter(Product.id_product == search_name)

        all_products = [products_product_name, products_seller_username, products_matching_ids]
        print(all_products[2].all())
        return render_template('products/search_product.html', title=search_name, products=all_products, form=form)

    def post(self, search_name):
        form = core_forms.ProductSearchForm()

        product_search = request.form.get('search_name')

        return redirect(url_for('products.search_product', search_name=product_search, form=form))
