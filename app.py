# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import render_template

from views.todos import todos_view

app = Flask(__name__)
app.register_blueprint(todos_view, url_prefix='/todos')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    return str(datetime.now())


@app.route('/1/ping')
def ping():
    """健康监测
    LeanEngine 会根据 `/1/ping` 判断应用是否正常运行。
    如果返回状态码为 200 则认为正常。
    其他状态码或者超过 5 秒没响应则认为应用运行异常。
    """
    return 'pong'
