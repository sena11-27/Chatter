from models.database import get_db

def create_thread(username, title, description):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO threads (username, title, description) VALUES (%s, %s, %s)", (username, title, description))
    db.commit()

def get_all_threads():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM threads ORDER BY created_at DESC")
    return cursor.fetchall()

def get_thread_by_id(thread_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM threads WHERE id = %s", (thread_id,))
    result = cursor.fetchall()
    if result:
        return result[0]
    return None

def get_posts_for_thread(thread_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM posts WHERE thread_id = %s ORDER BY created_at DESC", (thread_id,))
    return cursor.fetchall()

def delete_thread(thread_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM threads WHERE id = %s", (thread_id,))
    db.commit()
