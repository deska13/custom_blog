import sqlite3
from db.models import User


def get_users():
    conn = sqlite3.connect('C:/Users/deska/OneDrive/Рабочий стол/teach/learn_blog/custom_blog/db/example.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM users;""")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    users = []
    for row in rows:
        users.append(User(row[0], row[1], row[2], row[3]))
    return users


def get_user_by_id(id):
    conn = sqlite3.connect('C:/Users/deska/OneDrive/Рабочий стол/teach/learn_blog/custom_blog/db/example.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM users WHERE user_id={id};""")
    row = cur.fetchone()
    conn.commit()
    conn.close()
    return User(row[0], row[1], row[2], row[3])


def get_user(login):
    conn = sqlite3.connect('C:/Users/deska/OneDrive/Рабочий стол/teach/learn_blog/custom_blog/db/example.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM users WHERE f_name={login};""")
    row = cur.fetchone()
    conn.commit()
    conn.close()
    return User(row[0], row[1], row[2], row[3])


def insert_user(login, password, remember_me):
    conn = sqlite3.connect('C:/Users/deska/OneDrive/Рабочий стол/teach/learn_blog/custom_blog/db/example.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO users(f_name, password_hash, save_me) 
        VALUES(?,?,?);""", (login, password, remember_me))
    id = cur.lastrowid
    conn.commit()
    conn.close()
    return User(id, login, password, remember_me)


def delete_user(user_id):
    conn = sqlite3.connect('./db/example.db')
    cur = conn.cursor()
    cur.execute(f"""DELETE FROM users WHERE user_id={user_id};""")
    conn.commit()
    conn.close()