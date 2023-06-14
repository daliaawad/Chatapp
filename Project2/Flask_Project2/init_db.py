import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO logs (title, req_url) VALUES (?, ?)",
            ('First log', 'URL Content for the first log')
            )

cur.execute("INSERT INTO logs (title, req_url) VALUES (?, ?)",
            ('Second log', 'URL Content for the second log')
            )

connection.commit()
connection.close()