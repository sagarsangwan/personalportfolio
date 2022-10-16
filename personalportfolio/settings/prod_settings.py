import os
from re import T
from .base_settings import *
from dotenv import load_dotenv
import dj_database_url


load_dotenv('../.env')


DEBUG = False
# ALLOWED_HOSTS = ['.herokuapp.com',
#                  'teachothersonline.com', 'www.teachothersonline.com']

# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES = {
#     'default': db_from_env,
# }
# # added because of heroku giving error -app not found


STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
WHITENOISE_USE_FINDERS = True

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), ]
