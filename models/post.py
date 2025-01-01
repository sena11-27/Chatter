from models.database import get_db

def create_post(username, content, thread_id=None):
    db = get_db()
    db.execute('INSERT INTO posts (username, content, thread_id) VALUES (?, ?, ?)', (username, content, thread_id))
    db.commit()

def get_posts(thread_id):
    db = get_db()
    return db.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()

def delete_post(post_id):
    db = get_db()
    db.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    db.commit()