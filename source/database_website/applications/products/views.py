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
                                          seller_username=current_user.username,
                                          description=form.description.data,
                                          )

            flash('Added a product successfully!', category='success')
            return redirect(url_for('core.home_page'))

        else:
            return render_template(self.template_name, title=self.title, form=form)


class DisplayProductView(MethodView):
    def get(self, product_id):
        form = forms.DeleteProductForm()
        product = Product.query.get_or_404(product_id)
        return render_template('products/display_product.html', title=product.product_name, product=product, form=form)

    def post(self, product_id):
        form = forms.DeleteProductForm()
        product = Product.query.get_or_404(product_id)

        if form.delete.data:
            product.delete_product()
            return 'Product Has Been Deleted'

    # Optimize this


class SearchProductView(MethodView):
    def get(self, search_name, search_type):
        form = core_forms.ProductSearchForm()

        page = request.args.get('page', 1, type=int)
        all_results = form.get_results(search_name=search_name, search_type=search_type, page=page)

        next_url = url_for('products.search_product', page=all_results.next_num, search_name=search_name,
                           search_type=search_type) \
            if all_results.has_next else None

        prev_url = url_for('products.search_product', page=all_results.prev_num, search_name=search_name,
                           search_type=search_type) \
            if all_results.has_prev else None
        #  Possible optimisation needed

        return render_template('products/search_product.html',
                               title=search_name,
                               products=all_results.items,
                               form=form,
                               search_type=search_type,
                               search_name=search_name,
                               next_url=next_url,
                               prev_url=prev_url
                               )

    def post(self, search_name, search_type):
        form = core_forms.ProductSearchForm()

        product_search = request.form.get('search_name')
        product_type = request.form.get('search_type')

        return redirect(url_for('products.search_product', search_name=product_search, search_type=product_type,
                                form=form))
