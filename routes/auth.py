from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models.user import create_user, get_user_by_username, verify_password

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)
        
        if user and verify_password(user, password):
            session['username'] = username
            return redirect(url_for('home.index'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html')

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if get_user_by_username(username):
            flash('Username already exists', 'error')
        else:
            create_user(username, password)
            return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_blueprint.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.login'))
