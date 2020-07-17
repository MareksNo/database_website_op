from flask import Flask, render_template, url_for, flash, redirect, request
from flask.views import MethodView

from database_website.applications.views import FormViewMixin
from database_website.applications.products.models import Product
from database_website.applications.core import forms


class HomePageView(MethodView, FormViewMixin):

    def get(self):
        form = forms.ProductSearchForm()

        page = request.args.get('page', 1, type=int)
        products = Product.query.paginate(page, 20, False)

        next_url = url_for('core.home_page', page=products.next_num) \
            if products.has_next else None

        prev_url = url_for('core.home_page', page=products.prev_num) \
            if products.has_prev else None

        return render_template('core/home.html',
                               title='Home',
                               products=products.items,
                               form=form,
                               next_url=next_url,
                               prev_url=prev_url)

    def post(self):
        form = forms.ProductSearchForm()

        product_search = request.form.get('search_name')
        product_type = request.form.get('search_type')

        return redirect(url_for('products.search_product', search_name=product_search, search_type=product_type))
