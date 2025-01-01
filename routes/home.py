from flask import Blueprint, request, redirect, url_for, render_template, session
from models.post import create_post, get_posts, delete_post
from models.thread import get_all_threads, create_thread, get_thread_by_id, get_posts_for_thread  # get_posts_for_thread をインポート

home_blueprint = Blueprint('home', __name__)

def is_logged_in():
    """セッションにユーザー名が存在するか確認する共通関数"""
    return 'username' in session

@home_blueprint.route('/')
def index():
    threads = get_all_threads()  # スレッドを取得
    return render_template('index.html', threads=threads, username=session.get('username'))


@home_blueprint.route('/thread/<int:thread_id>')
def thread(thread_id):
    thread = get_thread_by_id(thread_id)  # スレッドの詳細を取得
    if thread is None:
        return "スレッドが見つかりません", 404  # スレッドがない場合、404エラーページにリダイレクト
    posts = get_posts_for_thread(thread_id)  # スレッドに関連する投稿を取得
    return render_template('thread.html', thread=thread, posts=posts, username=session.get('username'))

@home_blueprint.route('/create_thread', methods=['POST'])
def create_thread_route():
    """スレッド作成処理"""
    if not is_logged_in():
        return redirect(url_for('auth.login'))
    
    title = request.form['title']
    description = request.form['description']
    username = session['username']
    create_thread(title, description, username)  # スレッド作成
    return redirect(url_for('home.index'))  # スレッド一覧にリダイレクト

@home_blueprint.route('/post', methods=['POST'])
def create_post_route():
    """投稿作成処理"""
    if not is_logged_in():
        return redirect(url_for('auth.login'))
    
    content = request.form['content']
    username = session['username']
    thread_id = request.form['thread_id']
    create_post(username, content, thread_id)  # 投稿作成
    return redirect(url_for('home.thread', thread_id=thread_id))  # 投稿後にスレッド詳細ページにリダイレクト

@home_blueprint.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post_route(post_id):
    """投稿削除処理"""
    if not session.get('username'):
        return redirect(url_for('auth.login'))  # ログインしていなければログインページへ
    delete_post(post_id)  # 投稿削除
    return redirect(url_for('home.index'))  # 削除後にスレッド一覧にリダイレクト
