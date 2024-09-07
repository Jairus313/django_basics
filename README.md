# Django basic app tutorial

## Hey Everyone, this Python's Django RESTAPI framework brush-up tutorial for myself and also for you.

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

## Models in Django

Models are basically the definition of the database that will be used by the applications. Run below command to apply the DB changes of the application.

```
  python manage.py migrate
```

migrate command will go through the settings.py and make the necessary changes to the application and these changes will be shipped with app.

### Creating the models

Add the two tables for the poll app with name question(question that has been asked) and choice(selected choice from the user)

```python
  from django.db import models

  # Create your models here.
  class Question(models.Model):
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField("date published")


  class Choice(models.Model):
      question = models.ForeignKey(Question, on_delete=models.CASCADE)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)
```

"django.db.models.Model" will be the package that has everything need for data modeling. Each table in the database are classes which needs to be defined in the models.py. Class name will be the table name and variables inside will be the table's column. models sub-module will provide the metadata needed as mentioned above. Some example are:

- CharField will be character
- DateTimeField will be timestamp
- IntegerField will be integer
- ForeignKey will be foreign key

### Activating the models

Once the model is defined it needs to be activated in the app, to do so it needs to be added in the INSTALLED_APPS setting

```python
  INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "polls.apps.PollsConfig", # added to the application
  ]

```

After this step, application needs to be updated with it and this will be done by running the below command.

```
  python3 manage.py makemigrations
```

This make changes to the models of the application and a file will be generated according in the location polls/migrations/0001_initial.py. Since this file purpose is to detect the changes and record it in the file and needs to be applied by migrate command as below.

```
  python3 manage.py migrate
```
