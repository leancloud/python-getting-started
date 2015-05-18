# coding: utf-8

from leancloud import Object
from leancloud import Query
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template


class Todo(Object):
    pass

todos_view = Blueprint('todos', __name__)


@todos_view.route('')
def show():
    todos = Query(Todo).descending('createdAt').find()
    return render_template('todos.html', todos=todos)


@todos_view.route('', methods=['POST'])
def add():
    content = request.form['content']
    todo = Todo(content=content)
    todo.save()
    return redirect(url_for('todos.show'))
