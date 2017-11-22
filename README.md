# django-activity
Activity/Task simple tracker and state persistence for Django

You can install `django-activity` with `pip`

```
pip install git+git://github.com/feroda/django-activity#egg=activity
```
(remember to add the dependency in your requirements.txt if you are using virtualenvs)

add `activity` to `INSTALLED_APPS` in `settings.py`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ...
    'activity',
]
```