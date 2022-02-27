from flask_login import LoginManager
from flask import Flask, request, render_template, redirect, Blueprint


auth_page = Blueprint('auth_page', __name__, template_folder='templates')


login_manager = LoginManager()
# login_manager.init_app(app)


# @login_manager.user_loader
# def load_user(user_id):
#     for user in users:
#         if user.get_id() == user_id:
#             return user
#     return None