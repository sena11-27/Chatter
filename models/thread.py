from models.database import get_db

def create_thread(username, title, description):
    db = get_db()
    db.execute("INSERT INTO threads (username, title, description) VALUES (?, ?, ?)", (username, title, description))
    db.commit()

def get_all_threads():
    db = get_db()
    return db.execute("SELECT * FROM threads ORDER BY created_at DESC").fetchall()

def get_thread_by_id(thread_id):
    db = get_db()
    result = db.execute("SELECT * FROM threads WHERE id = ?", (thread_id,)).fetchall()
    if result:
        return result[0]
    return None

def get_posts_for_thread(thread_id):
    db = get_db()
    return db.execute("SELECT * FROM posts WHERE thread_id = ? ORDER BY created_at DESC", (thread_id,)).fetchall()

def delete_thread(thread_id):
    db = get_db()
    db.execute("DELETE FROM threads WHERE id = ?", (thread_id,))
    db.commit()