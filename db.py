import os
import sqlite3
from flask import g

from app import app

DATABASE = os.path.join(os.path.dirname(__file__), 'DB.db')

def get():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query(command, args=(), one=False):
    cur = get().execute(command, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def execute(command, args=(), one=False):
    cur = get().execute(command, args)
    cur.connection.commit()
    cur.close()

def init():
    with app.app_context():
        db = get()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    init()