from flask import Blueprint, request, redirect, url_for, render_template, session
from models.post import create_post, get_posts, delete_post

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts, username=session.get('username'))

@home_blueprint.route('/post', methods=['POST'])
def post():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    content = request.form['content']
    username = session['username']
    create_post(username, content)
    return redirect(url_for('home.index'))

@home_blueprint.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post_route(post_id):
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    delete_post(post_id)
    return redirect(url_for('home.index'))