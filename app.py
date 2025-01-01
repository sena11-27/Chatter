from flask import Flask, render_template, request, redirect, url_for, session, flash
from routes.home import home_blueprint
from routes.auth import auth_blueprint
from models.database import init_db
from routes.api import api_blueprint
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

init_db()
CORS(app)
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)