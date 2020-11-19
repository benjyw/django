import itertools
import os
from pathlib import PurePath

import django
from django.apps import apps
from django.conf import settings


def add_app(path):
    path_parts = PurePath(path).parts
    suffix_parts = list(itertools.dropwhile(lambda x: x != 'tests', path_parts))
    package = '.'.join(suffix_parts[1:-1])  # Omit the leading 'tests' and the filename.
    if package not in settings.INSTALLED_APPS:
        #print(f"PPPPPPPPPPP {package}")
        settings.INSTALLED_APPS.append(package)
    apps.set_installed_apps(settings.INSTALLED_APPS)


def pytest_collect_file(path, parent):
    add_app(path)
    return None  # Delegate to the standard collector.


def pytest_configure():
    configure_settings()


def configure_settings():
    settings.configure(
        SECRET_KEY="django_tests_secret_key",
        TIME_ZONE="UTC",
        USE_TZ=True,
        PROFILE=False,
        LANGUAGE_CODE='en',
        # Use a fast hasher to speed up tests.
        PASSWORD_HASHERS = [
            'django.contrib.auth.hashers.MD5PasswordHasher',
        ],
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django.contrib.sites',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.admin.apps.SimpleAdminConfig',
            'django.contrib.staticfiles',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            },
            'other': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },
        MIGRATION_MODULES={
            # This lets us skip creating migrations for the test models as many of
            # them depend on one of the following contrib applications.
            'auth': None,
            'contenttypes': None,
            'sessions': None,
        },
        TEMPLATES = [{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['tests/templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            }
        }]
    )

    #django.setup()
