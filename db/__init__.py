import sqlite3


def create_db():
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pets (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 age INT,
                 type TEXT,
                 created_at TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%S',  datetime('now', '3 hours')))
                 )''')
    conn.commit()
    conn.close()
