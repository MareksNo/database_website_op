from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

from database_website.exceptions import LoginException

from database_website.applications.users import forms
from database_website.applications.views import FormViewMixin
from database_website.applications.users import models


from flask.views import MethodView


class RegistrationView(MethodView, FormViewMixin):
    form_class = forms.RegisterForm
    template_name = 'users/register.html'
    title = 'Register'

    def post(self):
        form = self.get_form()  # getting the Register form from forms.py and setting to a variable

        if form.validate_on_submit():
            form.save()

            return redirect(url_for('users.login'))
        else:
            flash(f'Please Check your form', category='danger')
            return render_template(self.template_name, title=self.title, form=form)


class LoginView(MethodView, FormViewMixin):
    form_class = forms.LoginForm
    template_name = 'users/login.html'
    title = 'Login'

    def post(self):
        form = self.get_form()  # getting the LogIN form from forms.py and setting to a variable
        if form.validate_on_submit():
            user = models.User.query.filter_by(email=form.email.data).first()  # searching for the email

            try:
                form.login(user)
                return redirect(url_for('core.home_page'))

            except LoginException as exception:
                print(str(exception))

        flash('Wrong Credentials!', category='danger')
        return render_template(self.template_name, title=self.title, form=form)


class LogoutView(MethodView):
    decorators = [
        login_required,
    ]

    def get(self):
        return render_template('users/logout.html', title=f'{current_user.username} Logout')

    def post(self):
        logout_user()
        return redirect(url_for('users.login'))


class UserProfileView(MethodView):
    def get(self, user_id):
        user = models.User.query.get_or_404(user_id)

        return render_template('users/user_profile.html', title=f'{user.username} Profile', user=user)


class HomeView(MethodView):
    pass
