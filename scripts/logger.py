import sqlite3

def create_database():
    conn = sqlite3.connect('datasets/logs/user_interactions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            gender TEXT,
            language TEXT,
            domain1 TEXT,
            domain2 TEXT,
            domain3 TEXT,
            domain4 TEXT,
            general_test TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

create_database()