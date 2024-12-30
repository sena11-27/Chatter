from flask import Blueprint, request, jsonify
from models.post import create_post, get_posts, delete_post
from models.user import get_user_by_username

api_blueprint = Blueprint('api', __name__)

# 投稿の取得
@api_blueprint.route('/api/posts', methods=['GET'])
def api_get_posts():
    posts = get_posts()
    posts_list = [
        {"id": post["id"], "username": post["username"], "content": post["content"], "created_at": post["created_at"]}
        for post in posts
    ]
    return jsonify(posts_list)

# 投稿の作成
@api_blueprint.route('/api/posts', methods=['POST'])
def api_create_post():
    data = request.get_json()
    content = data.get('content')
    username = data.get('username')

    if not content or not username:
        return jsonify({"error": "Content and username are required"}), 400

    create_post(username, content)
    return jsonify({"message": "Post created successfully"}), 201

# 投稿の削除
@api_blueprint.route('/api/posts/<int:post_id>', methods=['DELETE'])
def api_delete_post(post_id):
    delete_post(post_id)
    return jsonify({"message": "Post deleted successfully"}), 200
