# coding: utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
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
    try:
        todos = Query(Todo).descending('createdAt').find()
    except LeanCloudError as e:
        if e.code == 101:  # Class does not exist on the cloud. 
            todos = []
        else:
            raise e
    return render_template('todos.html', todos=todos)


@todos_view.route('', methods=['POST'])
def add():
    content = request.form['content']
    todo = Todo(content=content)
    try:
        todo.save()
    except LeanCloudError as e:
        return e.error, 502
    return redirect(url_for('todos.show'))
