import os
from os.path import join
from envparse import env

BASE_DIR = os.path.dirname(__file__)

class Config(object):
    GENERATED_STATIC_URL_PATH = env('FLASK_GENERATED_STATIC_URL_PATH', default='/gen-static')

class DevelopmentConfig(Config):
    HOST = 'localhost'
    DEBUG = env('FLASK_DEBUG', cast=bool, default=True)
    RELOAD = True
    GENERATED_STATIC_DIR = join(BASE_DIR, 'generated-static')
    GENERATED_STATIC_URL_BASE = 'http://localhost:5000/'

class ProductionDockerConfig(Config):
    HOST = '0.0.0.0'
    DEBUG = env('FLASK_DEBUG', cast=bool, default=False)
    GENERATED_STATIC_DIR = '/var/generated-static/'
    GENERATED_STATIC_URL_BASE = env('FLASK_GENERATED_STATIC_URL_BASE', default='')
