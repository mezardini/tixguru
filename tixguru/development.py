from tixguru.settings import *

DEBUG = True

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*']




EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_SSL = env('EMAIL_USE_SSL')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')