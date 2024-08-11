# Django basic app

# Hey Everyone, this Python's Django RESTAPI framework brush-up tutorial for myself and also for you.

Everything that this repo has been covered from [official Django documentation](https://docs.djangoproject.com/en/5.1/).

Before starting up, make sure you have created virtual environment for the project. Follow [my article](https://medium.com/analytics-vidhya/python-virtual-environment-in-nutshell-abc74482fbd1)(windows) or [official documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)(macos/linux), if you are new to it.

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
python3 manage.py migrate
```

Now that project has been set-up, create the application of the project.

> [!NOTE]
> What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

Use below command to create the app

```
python3 manage.py startapp polls
```

This will create the base template/boiler-plate for the djanog project, this folder would consists below files

- polls:
  - migrations/
    - init.py: Contains migration files that track changes to the models and apply them to the database.
  - init.py: Makes this folder as package
  - admin.py: Registers your models with the Django admin site and customizes the appearance of models in the admin interface.
  - apps.py: Contains the configuration for the app. It defines the app's name and provides metadata about the app.
  - models.py: Defines the data models (database schema) for the app. Each model represents a table in the database.
  - tests.py: Contains test cases for the app, ensuring the code works as expected(TDDs).
  - views.py: Contains view functions or classes that requests and return responses. It connects the models, templates, and forms with the business logic of the application.

## Adding the endpoint with it's functionality

Once the app is created add the functionality in the views via creating function for it. e.g:

```python
def index(request):
    return HttpResponse("Index page")
```

and register the view with it's end-point in URLs file:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index") # new url here
]
```
