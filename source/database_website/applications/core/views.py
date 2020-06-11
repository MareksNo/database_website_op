from flask import Flask, render_template, url_for, flash, redirect, request
from flask.views import MethodView

from database_website.applications.views import FormViewMixin
from database_website.applications.products.models import Product
from database_website.applications.core import forms


class HomePageView(MethodView, FormViewMixin):

    def get(self):
        form = forms.ProductSearchForm()
        products = Product.query.all()
        return render_template('core/home.html', title='Home',  products=products, form=form)

    def post(self):

        product_search = request.form.get('search_name')

        return redirect(url_for('products.search_product', search_name=product_search))
