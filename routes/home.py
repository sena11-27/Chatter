from flask import Blueprint, request, redirect, url_for, render_template, session
from models.post import create_post, get_posts, delete_post, get_post_by_id
from models.thread import get_all_threads, create_thread, get_thread_by_id, get_posts_for_thread, delete_thread

home_blueprint = Blueprint('home', __name__)

def is_logged_in():
    return 'username' in session

@home_blueprint.route('/')
def index():
    threads = get_all_threads()
    return render_template('index.html', threads=threads, username=session.get('username'))


@home_blueprint.route('/thread/<int:thread_id>')
def thread(thread_id):
    thread = get_thread_by_id(thread_id)  
    if thread is None:
        return "スレッドが見つかりません", 404  
    posts = get_posts_for_thread(thread_id) 
    return render_template('thread.html', thread=thread, posts=posts, username=session.get('username'))

@home_blueprint.route('/create_thread', methods=['POST'])
def create_thread_route():
    if not is_logged_in():
        return redirect(url_for('auth.login'))
    
    title = request.form['title']
    description = request.form['description']
    username = session['username']
    create_thread(title, description, username) 
    return redirect(url_for('home.index'))  

@home_blueprint.route('/post', methods=['POST'])
def create_post_route():
    if not is_logged_in():
        return redirect(url_for('auth.login'))
    
    content = request.form['content']
    username = session['username']
    thread_id = request.form['thread_id']
    create_post(username, content, thread_id)  
    return redirect(url_for('home.thread', thread_id=thread_id))  

@home_blueprint.route('/delete_thread/<int:thread_id>', methods=['POST'])
def delete_thread_route(thread_id):
    delete_thread(thread_id)
    return redirect(url_for('home.index'))

@home_blueprint.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post_route(post_id):
    if not session.get('username'):
        return redirect(url_for('auth.login'))

    post = get_post_by_id(post_id)
    if post and post['username'] == session['username']:
        delete_post(post_id) 
    return redirect(url_for('home.thread', thread_id=post['thread_id']))
