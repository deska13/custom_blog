from flask import Flask, request, render_template, redirect, Blueprint


article_page = Blueprint('article_page', __name__, template_folder='templates')


@article_page.route("/", methods=["GET", "POST"])
def index():
    articles = []
    return render_template("index.html", articles=articles)