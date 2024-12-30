import sqlite3

def init_db():
    with open('schema.sql', 'r') as f:
        schema = f.read()

    conn = sqlite3.connect('board.db')
    conn.cursor().executescript(schema)
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect('board.db')
    conn.row_factory = sqlite3.Row
    return conn
