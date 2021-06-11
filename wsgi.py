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

    if os.environ['LEANCLOUD_APP_ENV'] == 'production':
        class NopLogger(object):
            def write(self, _):
                pass

        server = WSGIServer(('', PORT), application, log=NopLogger(), handler_class=WebSocketHandler)
        server.serve_forever()

    else:
        from werkzeug.serving import run_with_reloader
        from werkzeug.debug import DebuggedApplication

        @run_with_reloader
        def run():
            global application
            app.debug = True
            application = DebuggedApplication(application, evalex=True)
            server = WSGIServer(('localhost', PORT), application, handler_class=WebSocketHandler)
            server.serve_forever()

        run()
