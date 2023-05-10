import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


def estab_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(pid):
    conn = estab_connection()
    getsinglepost = conn.execute(
        'SELECT * FROM posts WHERE id = ?', (pid,)).fetchone()
    conn.close()

    if post is None:
        abort(404)
    return getsinglepost


bpp = Flask(__name__)
bpp.secret_key = 'it is a secret'
bpp.config['SECRET KEY'] = 'SE blog'


@bpp.route('/')
def blogintro():
    conn = estab_connection()
    getpost = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('intro.html', posts=getpost)


@bpp.route('/<int:pid>')
def post(pid):
    post = get_post(pid)
    return render_template('post.html', post=post)


@bpp.route('/about')
def about():
    return render_template('about.html')


@bpp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        newtitle = request.form['title']
        newcontent = request.form['content']

        if not newtitle:
            flash("Title is required")
        else:
            conn = estab_connection()
            conn.execute('INSERT INTO posts(title,content) VALUES (?,?)', (newtitle, newcontent))
            conn.commit()
            conn.close()

        return redirect(url_for('blogintro'))

    return render_template('create.html')


# connection established but updation not invoked
@bpp.route('/<int:pid>/edit', methods=('GET', 'POST'))
def edit(pid):
    post = get_post(pid)

    bl=0

    if request.method == 'POST':
        newtitle = request.form['title']
        newcontent = request.form['content']
        created = post['created']

        if not newtitle:
            flash('Title is Required')
        elif newcontent == '':
            flash('Content is Empty')
        else:

            notallowed = "*?!'^+%&/()=}][{$#0123456789"
            for char in newcontent:
                if char in notallowed:
                    
                    bl = 1
                    break

            if bl == 1:
                flash('content is not valid')

            else:
                conn = estab_connection()
                conn.execute('UPDATE posts SET title = ?, content = ?, created = ?' 'WHERE id = ?', (newtitle, newcontent, created, pid))
                conn.execute('SELECT * FROM posts ORDER BY created DESC')
                conn.commit()
                conn.close()
                return redirect(url_for('blogintro'))

    return render_template('edit.html', post=post)





    return redirect(url_for('blogintro'))
