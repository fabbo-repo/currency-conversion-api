# DRF API

## Environment Variables

| NAME                      | DESCRIPTION                                                |
| ------------------------- | ---------------------------------------------------------- |
| APP_DEBUG                 | Debug mode enabled (true|false)                            |
| APP_ALLOWED_HOSTS         | List of strings representing the allowed host/domain names |
| APP_CORS_HOSTS            | CORS allowed host/domain names                             |
| DATABASE_URL              | Databse url                                                |
| DEFAULT_API_KEY           | Default value for API Key (uuid)                           |
| CURRENCY_CODES            | Currency codes allowed (they have to be valid)             |
| MAX_STORED_DAYS           | Max number of days without removing conversions            |
| MAX_NO_UPDATED_MINS       | Max number of minutos without fetching new conversions     |

## Error Codes

| CODE              | DEFINITION                                                 | ENDPOINT                       |
| ----------------- | ---------------------------------------------------------- | ------------------------------ |
| 1                 | Currency code not supported                                | /conversion/{code}             |
| 2                 | Too many days to fetch conversions                         | /conversion/days/{days}        |

## Directory tree example

~~~bash
djangorest/
    ├── app_1/
    │   ├── management/
    |   |   ├── __init__.py
    │   │   └── commands/
    |   |       ├── __init__.py
    |   |       ├── schedule_setup.py
    │   │       └── ... (This is optional)
    │   ├── templates/
    │   │   └── ... (This is optional)
    │   ├── migrations/
    │   │   └── ...
    |   ├── tests/
    |   │   ├── __init__.py
    |   │   ├── tests_1.py
    |   │   └── ...
    │   ├── api/
    |   │   ├── serializers.py  (This is optional)
    |   │   ├── serializers/
    │   |   │   ├── model1_serializers.py
    │   |   │   ├── ... (This is optional)
    │   |   │   └── model2_serializers.py
    |   │   ├── views.py  (This is optional)
    |   │   ├── views/
    │   |   │   ├── model1_views.py
    │   |   │   ├── ... (This is optional)
    │   |   │   └── model2_views.py
    |   │   └── urls.py
    │   ├── __init__.py
    │   ├── tasks.py
    │   ├── signals.py
    │   ├── schedule_setup.py
    │   ├── models.py
    │   ├── filters.py
    │   ├── notifications.py
    │   ├── apps.py
    │   ├── exceptions.py
    │   └── admin.py
    ├── ...
    ├── app_2/
    │   ├── ...
    │   └── external_api_name_integration.py
    ├── external_api_name/
    │   ├── __init__.py
    │   ├── client.py
    │   └── django_client.py
    ├── core/
    |   ├── tests/
    |   │   ├── __init__.py
    |   │   ├── tests_settings.py
    |   │   └── ...
    |   ├── swagger/
    |   │   ├── __init__.py
    |   │   └── urls.py
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── celery.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── api_urls.py
    │   ├── exceptions.py
    │   └── wsgi.py
    ├── templates/
    │   └── ... (This is optional)
    ├── media/
    │   └── ... (This is optional)
    ├── static/
    │   └── ... (This is optional)
    ├── manage.py
    └── db.sqlite3
~~~

## Useful commands

* Install project requirements:

~~~bash
pip install -r requirements.txt
~~~

* For the project creation it was used:

~~~bash
django-admin startproject core
~~~

* Create migrations:

~~~bash
python manage.py makemigrations
~~~

* Migrate changes (create tables in the specified database):

~~~bash
python manage.py migrate
~~~

* Check On Premise settings:

~~~bash
python manage.py check-on-premise
~~~

* Create folder for static files:

~~~bash
python manage.py collectstatic
~~~

* Create an app:

~~~bash
python manage.py startapp app_1
~~~

* Create superuser:

~~~bash
python manage.py createsuperuser
~~~

* Change password:

~~~bash
python manage.py changepassword <username>
~~~

* Run server in debug mode:

~~~bash
python manage.py runserver 
~~~

* Export db data to a json file:

~~~bash
python manage.py dumpdata > db.json
~~~

* Import db data from a json file:

~~~bash
python manage.py loaddata db.json
~~~

* Launch testing: (coverage included)

~~~bash
python manage.py test
~~~

* Generate html with coverage report:

~~~bash
coverage html
~~~

* Generate locale messages files

~~~bash
django-admin makemessages --all --ignore=en
~~~

> Before executing it, a locale folder with all languages folders inside must be created

* Generate compiled messages

~~~bash
django-admin compilemessages --ignore=env
~~~