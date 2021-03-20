import os
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '$sool69_c@_iti!y7(*#z)j))-nq5ra-6npl89@!4f2xxttqun'

# Deploy Part
DEBUG = True
ALLOWED_HOSTS = ['megacoders.ir', 'www.megacoders.ir', '127.0.0.1', 'localhost']
# SECURE_SSL_REDIRECT = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps
    'accounts.apps.AccountsConfig',
    # 'blog.apps.BlogConfig',
    'core.apps.CoreConfig',
    # 'learn.apps.LearnConfig',

    # Third-Party Apps
    'crispy_forms',
    'widget_tweaks',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'mysql.connector.django',
#         'NAME': 'megacod2_thisismegacoders2',
#         'USER': 'megacod2_Amir-Mohamad2',
#         'PASSWORD': '85=[~,H+8Eyx',
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'accounts.User'
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'accounts.authentication.EmailBackend',
# ]
LOGIN_URL = reverse_lazy('accounts:login')
LOGIN_REDIRECT_URL = reverse_lazy('core:home')
LOGOUT_URL = reverse_lazy('accounts:logout')
LOGOUT_REDIRECT_URL = reverse_lazy('core:home')



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATIC_ROOT = '/home/megacod2/public_html/static/'
STATICFILES_DIRS = [BASE_DIR, "static"]


MEDIA_ROOT = '/home/megacod2/public_html/media/'
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CONTENT_TYPES = {'image'}
MAX_UPLOAD_SIZE = 2097152 # 2 MB (2000000)  
VALID_FORMATS = {'jpeg', 'jpg', 'png'}


# Email Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.megacoders.ir'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'support@megacoders.ir'
EMAIL_HOST_PASSWORD = '4PBN+ntvG88h!6'

# Sweet Alert packge

# Arvan Cloud or Araz Cloud 
