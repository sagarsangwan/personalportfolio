from .base_settings import *
import dj_database_url

DEBUG = True
# ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', ]


WHITENOISE_USE_FINDERS = True

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
