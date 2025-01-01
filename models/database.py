import psycopg2
from config import Config

DATABASE_URI = Config.DATABASE_URI  

def get_db():
    conn = psycopg2.connect(DATABASE_URI)
    conn.autocommit = True  
    return conn

def init_db():
    with open('schema.sql', 'r') as f:
        schema = f.read()

    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(schema) 
    finally:
        conn.close()

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
