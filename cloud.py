# coding: utf-8

from leancloud import Engine

engine = Engine


@engine.cloud_func
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'
