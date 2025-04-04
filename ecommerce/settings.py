"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'
# # Là c'est la racine du projet.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# C'est la clé secrete du projet. Chaque projet django a une clé secrete
SECRET_KEY = 'django-insecure-bnx8lej#u$wahwy#^eo+$l8p0q54ph_6od2(6ridpx4!9_p&nn'
# SECURITY WARNING: don't run with debug turned on in production!

#Cette doit etre mise sur false quand on déploie pour que les erreurs ne s'affichent pas du coté de l'utilisateur
DEBUG = True

#ALLOWED_HOSTS nous permet de donner le domaine d'acces à l'application
ALLOWED_HOSTS = []


# Application definition
# INSTALLED_APPS  contient la liste de nos applications. On y rajoute des applications, c'est à dire un composant
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# les MIDDLEWARE sont des bouts de code qui permettent de gerrer une partie spécifique de l'application par exemple la sécurité, les sessions, etc
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# LE ROOT_URLCONF permet d'ouvrir le site dans le navigateur. Il gere tout ce qui est routage
ROOT_URLCONF = 'ecommerce.urls'

# Le TEMPLATES gere tout ce qui est configuration html. Il permet à notre application de savoir où se trouve nos fichiers html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
#Notre application tourne sur le serveur WSGI par défaut
WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#Ici c'est pour la configuration de la base de données: on peut utiliser n'importequelle(mysql, mongodb, postgres, etc)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
#Gestionnaire de la validation des motes de passes
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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# Ici on gere tout ce qui est internationalisation
LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

#ici on les fichiers static : CSS, JavaScript, Images
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

#L'incrementation quand on rajoute des choses dans la base de données
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
