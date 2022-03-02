from flask import Flask, request, render_template, redirect, Blueprint
from db.queries.article_query import *


article_page = Blueprint('article_page', __name__, template_folder='templates')


@article_page.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", articles=get_articles())


@article_page.route("/add_article", methods=["GET", "POST"])
def add_article():
    if request.method == "GET":
        return render_template("article/add_article.html")
    else:
        insert_article(
            request.form['title'], 
            request.form['content']
        )
        return redirect("/")


@article_page.route("/delete_article/<int:id>", methods=["GET", "POST"])
def delete_article(id):
    delete_article_by_id(id)
    return redirect("/")