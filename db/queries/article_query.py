import sqlite3
from db.models import Article
from flask_login import current_user

from db.queries.user_query import get_user_by_id


def get_articles():
    conn = sqlite3.connect('C:/Users/deska/OneDrive/Рабочий стол/teach/learn_blog/custom_blog/db/example.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM articles;""")
    rows = cur.fetchall()
    
    articles = []
    for row in rows:
        user = get_user_by_id(row[1])
        articles.append(Article(
            row[0],
            row[2],
            row[3],
            user
        ))
    conn.commit()
    conn.close()
    return articles


def get_article(article_id):
    conn = sqlite3.connect('C:/Users/deska/OneDrive/Рабочий стол/teach/learn_blog/custom_blog/db/example.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM articles WHERE article_id={article_id};""")
    row = cur.fetchone()
    
    cur.execute(f"""SELECT * FROM user WHERE user_id={row[1]};""")
    user = cur.fetchone()
    article = Article(
        row[0],
        row[2],
        row[3],
        user[1]
    )
    conn.commit()
    conn.close()
    return article


def insert_article(title, content):
    conn = sqlite3.connect('C:/Users/deska/OneDrive/Рабочий стол/teach/learn_blog/custom_blog/db/example.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO articles(user_id, title, content) 
        VALUES(?,?,?);""", (current_user.id, title, content))
    conn.commit()
    conn.close()


def delete_article_by_id(article_id):
    conn = sqlite3.connect('./db/example.db')
    cur = conn.cursor()
    cur.execute(f"""DELETE FROM articles WHERE article_id={article_id};""")
    conn.commit()
    conn.close()