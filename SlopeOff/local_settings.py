import os

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = '%%e8kdr0=z*12$8vi1if8gwaev3zxbcgqrw&+=@m4)%-rzc96*'
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
