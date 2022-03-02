from flask_login import UserMixin
from werkzeug.security import check_password_hash


class User(UserMixin):
    def __init__(self, id, login, password, remember_me = False):
        print(id, login, password)
        self.id = id
        self.login = login
        self.password = password
        self.remember_me = remember_me


    def get_login(self):
        return self.login


    def get_password(self):
        return self.password


    def check_user(self, login, password):
        if login == self.login:
            return check_password_hash(self.password, password)
        return False