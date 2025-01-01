from flask import Flask, render_template, request, redirect, url_for, session, flash
from routes.home import home_blueprint
from routes.auth import auth_blueprint
from routes.api import api_blueprint
from flask_cors import CORS
import psycopg2
from config import Config

app = Flask(__name__)
app.config.from_object(Config) 

def get_db_connection():
    connection = psycopg2.connect(app.config['DATABASE_URI'])
    return connection

CORS(app)

app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    with open('schema.sql', 'r') as f:
        schema_sql = f.read()
    
    cursor.execute(schema_sql)
    
    connection.commit()
    cursor.close()
    connection.close()

init_db()

if __name__ == "__main__":
    app.run(debug=True)
