from models.database import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    hashed_password = generate_password_hash(password)
    db = get_db()
    db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    db.commit()

def get_user_by_username(username):
    db = get_db()
    return db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

def verify_password(user, password):
    return check_password_hash(user['password'], password)
