import sqlite3
ln = '\n'
con = sqlite3.connect("mememacicky.db")
cursor = con.cursor()
images = cursor.execute("""SELECT rowid, * FROM images""").fetchall()
print("all content of mememacicky images:")
for row in images:
    rowid = row[0]
    url = row[1]
    prompt = row[2]
    print(f"{rowid:02d} | {url} <-- {prompt}")
