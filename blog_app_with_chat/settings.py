import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'c@t9q-k__6+4sskjqna23xj4s&j-!dw0^j0e0b8vtqcd5=edu5'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party apps
    'channels',
    'social_django',

    # user defined apps
    'app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 3rd party middlewares
    'social_django.middleware.SocialAuthExceptionMiddleware',
]
ROOT_URLCONF = 'blog_app_with_chat.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 3rd party context procesers
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
WSGI_APPLICATION = 'blog_app_with_chat.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE =  'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOGIN_REDIRECT_URL = '/'
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AVATARS = os.listdir(os.path.join(STATICFILES_DIRS[0], 'images'))

# Social login backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)
# Dont put this here
SOCIAL_AUTH_GITHUB_KEY = 'b8860b7af7703489e5e7'
SOCIAL_AUTH_GITHUB_SECRET = 'f13d5170a6bb8fcafea21f94391625edfc23284e'

# channel settings
redis_host = os.environ.get('REDIS_HOST', 'localhost')
CHANNEL_LAYERS = {
    "default": {
        # This example app uses the Redis channel layer implementation channels_redis
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(redis_host, 6379)],
        },
    },
}
ASGI_APPLICATION = 'blog_app_with_chat.routing.application'



