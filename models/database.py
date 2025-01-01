import sqlite3

DATABASE = 'board.db'  # データベースファイルのパス

def init_db():
    """データベースの初期化関数"""
    with open('schema.sql', 'r') as f:
        schema = f.read()  # schema.sql の内容を読み込む

    # データベースに接続してスキーマを実行
    with sqlite3.connect(DATABASE) as conn:
        conn.cursor().executescript(schema)
        conn.commit()  # 変更をコミット

def get_db():
    """データベース接続を取得する関数"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 結果を辞書形式で取得
    return conn

def execute_query(query, params=()):
    """単一のSQLクエリを実行する関数"""
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    finally:
        conn.close()

def execute_fetchall(query, params=()):
    """SQLクエリを実行して、全ての結果を取得する関数"""
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    finally:
        conn.close()
