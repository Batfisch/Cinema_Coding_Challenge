import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('Secret_Key') or 'ure-not-able-to-guess'
    WTF_CSRF_SECRET_KEY = SECRET_KEY
