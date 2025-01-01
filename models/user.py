from models.database import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    hashed_password = generate_password_hash(password)
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
    db.commit()

def get_user_by_username(username):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    result = cursor.fetchone()
    if result:
        return {'id': result[0], 'username': result[1], 'password': result[2]}
    return None

def verify_password(user, password):
    return check_password_hash(user['password'], password)
