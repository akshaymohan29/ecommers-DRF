from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'Ecommers',
#         'OPTIONS': {
#             'options': '-c search_path=django,customer'
#         },
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     },

# }

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME':'Ecommers',

        'USER': 'postgres',

        'PASSWORD': 'admin',

        'HOST': '127.0.0.1',

        'PORT': '5432',

    }

}