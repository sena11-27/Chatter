from models.database import get_db

def create_post(username, content, thread_id=None):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO posts (username, content, thread_id) VALUES (%s, %s, %s)', (username, content, thread_id))
    db.commit()

def get_posts(thread_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM posts WHERE thread_id = %s ORDER BY created_at DESC', (thread_id,))
    return cursor.fetchall()

def delete_post(post_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM posts WHERE id = %s', (post_id,))
    db.commit()

def get_post_by_id(post_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM posts WHERE id = %s', (post_id,))
    result = cursor.fetchall()
    if result:
        return result[0]
    return None
