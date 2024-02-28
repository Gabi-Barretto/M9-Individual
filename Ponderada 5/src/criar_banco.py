import sqlite3

conn = sqlite3.connect('dados.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor TEXT NOT NULL
)
''')
conn.commit()
conn.close()
