# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

import os

import leancloud

from app import app
from cloud import engine

APP_ID = os.environ['LEANCLOUD_APP_ID']
APP_KEY = os.environ['LEANCLOUD_APP_KEY']
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']
PORT = int(os.environ['LEANCLOUD_APP_PORT'])

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
# Set this to be True if you need to access LeanCloud services with Master Key.
leancloud.use_master_key(False)

# Uncomment the following line to redirect HTTP requests to HTTPS.
# app = leancloud.HttpsRedirectMiddleware(app)
app = engine.wrap(app)
application = app

if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    from geventwebsocket.handler import WebSocketHandler

    env = os.environ['LEANCLOUD_APP_ENV']
    if env == 'production':
        server = WSGIServer(('0.0.0.0', PORT), application, log=None, handler_class=WebSocketHandler)
        server.serve_forever()
    else:
        from werkzeug.serving import run_with_reloader
        from werkzeug.debug import DebuggedApplication

        app.debug = True
        application = DebuggedApplication(application, evalex=True)
        address = 'localhost' if env == 'development' else '0.0.0.0'
        server = WSGIServer((address, PORT), application, handler_class=WebSocketHandler)
        run_with_reloader(server.serve_forever)
