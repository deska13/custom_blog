from flask import Flask, request, render_template, redirect, Blueprint
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


auth = Blueprint('auth', __name__, template_folder='templates')


class LoginForm(FlaskForm):
    login = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit_button = SubmitField("Войти")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        remember_me = form.remember_me.data
        users = []
        for user in users:
            if user.check_user(login, password):
                login_user(user, remember=remember_me)
                return redirect("/")
    return render_template("login.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")