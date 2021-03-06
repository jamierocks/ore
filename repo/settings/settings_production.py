import os
from settings import settings

# Grab this from the environment as to not expose production secret key
settings['cookie_secret'] = os.environ.get('SECRET_KEY')


settings['db_user'] = os.environ.get('DB_USER')
settings['db_password'] = os.environ.get('DB_PASSWORD')
settings['db_host'] = os.environ.get('DB_PORT_5432_TCP_ADDR')
settings['db_port'] = os.environ.get('DB_PORT_5432_TCP_PORT')
settings['db_db'] = os.environ.get('DB_USER')
