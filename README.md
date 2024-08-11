# django_basics

## Start the project by using below command

```
django-admin startproject mysite
```

Above command will set-up the initial template for the Django project with name 'mysite'. This folder will basically consists of manage.py and mysite folder with init.py, settings.py, urls.py, asgi.py and wsgi.py

Descripition of files:

- manage.py: acts as command-line utility for the project where it will act as administrative tasks.
- mysite:
  - init.py: Makes this folder as package
  - settings.py: Configuration of the project
  - urls.py: URLs and endpoint declarations of the project
  - asgi.py: Asynchronous server compactible entry-point
  - wsgi.py: Web server compactible entry-point

## Start the server

To start the django the web server, navigate to mysite folder where manage.py is located and run below command

```
python3 manage.py runserver
```

> [!NOTE]
> migrate before starting out the server to be updated with DB models, use below command to do it

```
python manage.py migrate
```
