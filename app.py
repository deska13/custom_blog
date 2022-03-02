from flask import Flask, request, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from route.article_page import article_page
from route.auth import auth
from db.queries import get_users

app = Flask(__name__)
app.register_blueprint(article_page)
app.register_blueprint(auth)


app.config["SECRET_KEY"] = "matinf-secret"


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    users = get_users()
    for user in users:
        if user.get_id() == user_id:
            return user
    return None