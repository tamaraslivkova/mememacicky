import sqlite3
con = sqlite3.connect("mememacicky.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE images (
    url TEXT NOT NULL,
    prompt TEXT
);""")
