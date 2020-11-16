from pathlib import PurePath

import django
from django.apps import apps
from django.conf import settings


test_apps = set()

def pytest_collection_modifyitems(session, config, items):
    test_modules = set()
    for item in items:
        path_parts = PurePath(item.fspath).parts
        if path_parts[-1] == 'tests.py':
            test_modules.add(path_parts[-2])
    settings.INSTALLED_APPS.extend(list(sorted(test_modules)))
    apps.set_installed_apps(settings.INSTALLED_APPS)


settings.configure(
    SECRET_KEY="TEST_SECRET_KEY",
    TIME_ZONE="UTC",
    USE_TZ=True,
    PROFILE=False,
    LANGUAGE_CODE='en',
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sites',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.admin.apps.SimpleAdminConfig',
        'django.contrib.staticfiles',
        #'absolute_url_overrides'
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    }
)

django.setup()
