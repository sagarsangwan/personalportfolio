import os
from re import T
from .base_settings import *
from dotenv import load_dotenv
import dj_database_url


load_dotenv("../.env")


DEBUG = False
ALLOWED_HOSTS = [".vercel.app", "sagarsangwan.vercel.app", ".now.sh"]
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")
