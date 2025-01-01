from models.database import execute_query, execute_fetchall

def create_thread(username, title, description):
    query = "INSERT INTO threads (username, title, description) VALUES (?, ?, ?)"
    execute_query(query, (username, title, description))

def get_all_threads():
    query = "SELECT * FROM threads ORDER BY created_at DESC"
    return execute_fetchall(query)

def get_thread_by_id(thread_id):
    query = "SELECT * FROM threads WHERE id = ?"
    result = execute_fetchall(query, (thread_id,))
    if result:
        return result[0]  # 1件だけ取得
    return None


def get_posts_for_thread(thread_id):
    query = "SELECT * FROM posts WHERE thread_id = ? ORDER BY created_at DESC"
    return execute_fetchall(query, (thread_id,))


