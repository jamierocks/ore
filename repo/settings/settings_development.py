from settings import settings
from tornado.options import options

settings['debug'] = True

settings['cookie_secret'] = 'SUCH_SECURE_WOW'

settings['db_user'] = 'admin'
settings['db_password'] = 'password'
settings['db_host'] = 'localhost'
settings['db_port'] = '5432'
settings['db_db'] = 'repo'
