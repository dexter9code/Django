from storefront.settings.dev import DEBUG, SECRET_KEY
from .common import *
import os

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = []
