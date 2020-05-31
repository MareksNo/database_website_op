from flask import Flask, render_template, url_for, flash, redirect, request
from flask.views import MethodView

from database_website.applications.views import FormViewMixin
from database_website.applications.products.models import Product
from database_website.applications.core import forms
from database_website.application import application


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def sitemap():
    links = []
    for rule in application.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return links

class HomePageView(MethodView, FormViewMixin):

    def get(self):
        form = forms.ProductSearchForm()
        products = Product.query.all()
        return render_template('core/home.html', title='Home',  products=products, form=form)

    def post(self):

        product_search = request.form.get('search_name')

        return redirect(url_for('products.search_product', search_name=product_search))
