import sqlite3

conn = sqlite3.connect('./db/example.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    f_name TEXT,
    password_hash TEXT,
    save_me TEXT);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS articles(
    article_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INT NOT NULL,
    title TEXT,
    content TEXT);
""")
conn.commit()
conn.close()