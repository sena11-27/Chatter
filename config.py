import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    DATABASE_URI = 'postgresql://sena:password@localhost/chatterdatabase'
