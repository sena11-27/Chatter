import sqlite3

DATABASE = 'board.db' 

def init_db():
    with open('schema.sql', 'r') as f:
        schema = f.read()

    with sqlite3.connect(DATABASE) as conn:
        conn.cursor().executescript(schema)
        conn.commit() 

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row 
    return conn

def execute_query(query, params=()):
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    finally:
        conn.close()

def execute_fetchall(query, params=()):
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    finally:
        conn.close()
