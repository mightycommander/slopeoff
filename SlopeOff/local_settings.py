from settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'resort_info'),
        'USER': os.environ.get('DB_USER', 'mmardle'),
        'PASSWORD': os.environ.get('DB_PASS', 'defcon33'),
        'HOST': 'localhost',
        'PORT': '5432'

    }
}
