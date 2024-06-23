import sqlite3


def _dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_connection():
    con = sqlite3.connect("data/todo.db")
    con.row_factory = _dict_factory
    return con


def get_all_todos():
    con = get_connection()
    cur = con.cursor()
    result = cur.execute("SELECT id, title, status FROM todo")
    return result.fetchall()


def add_todo(title):
    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO todo (title, status) VALUES (?, 'todo');", (title,))
    con.commit()
    result = cur.execute("SELECT last_insert_rowid() AS id;")
    return result.fetchone()["id"]


def finish_todo(todo_id):
    con = get_connection()
    cur = con.cursor()
    cur.execute("UPDATE todo SET status = 'done' WHERE id = ?;", (todo_id,))
    con.commit()


def delete_all_todos():
    con = get_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM todo;")
    con.commit()
