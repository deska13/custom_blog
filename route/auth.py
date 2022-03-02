from flask import Flask, request, render_template, redirect, Blueprint
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from db.models.user import User
from db.queries import get_user, insert_user
# from app import load_user
from werkzeug.security import generate_password_hash


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
        try:
            user = get_user(login)
            if user.check_user(login, password):
                login_user(user, remember=remember_me)
                return redirect("/")
        except:
            pass
    return render_template("auth/login.html", form=form)


@auth.route("/registration", methods=["GET", "POST"])
def registration():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = generate_password_hash(form.password.data)
        remember_me = form.remember_me.data
        user = insert_user(login, password, remember_me)
        if user.check_user(login, password):
            login_user(user, remember=remember_me)
            return redirect("/")
    return render_template("auth/registration.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")