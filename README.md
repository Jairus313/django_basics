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
  python3 manage.py migrate
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

Once the migrated, you are good to go. Now you can leverage the "Question" and "Choice" classes for data purpose.

### Interacting and Modifying with the models

In Django you will get the interactive shell to use terminal to execute the code by running below coomand.

```
  python3 manage.py shell
```

[Click here](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#playing-with-the-api) to know more and also add rows to Question and Choice tables.

Here you can also add custom functions to the model classes to modify the functionality as you needed. Let's **str**() to display the text for both the classes.

```python
  class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # modify the str method to display question text
    def __str__(self):
        return self.question_text

  class Choice(models.Model):
      question = models.ForeignKey(Question, on_delete=models.CASCADE)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)

      # modify the str method to display question text
      def __str__(self):
          return self.choice_text
```

This will help us out to display the text that has been inserted to the table and you can just call it as below.

```
python3 manage.py shell

>>> from polls.models import Choice, Question

>>> Question.objects.filter(id=1)

>>> Choice.objects.filter(pk=1)
```

You can also add the custom functionality, as below and can be used just by calling out the function name.

```python
  class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

```
$ python3 manage.py shell

>>> from polls.models import Question

>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
```

### Django Admin page

Django admin is interactive dashboard that is built-in Django and can be used to manage the database, it be simply accessed by adding "admin" in the index URL but before that let's register user to the dashboard first. This can be done ny running the below command.

```
  $ python3 manage.py createsuperuser
```

This will ask for Username, Email and Password of your choice. Once you are done with this, just start the application again and open URL "[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)". To know more [click here](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#creating-an-admin-user)

### Adding Views

Now let's add some additional views that are required, Views are basically the functionality that are going to perform business logic of the application. Just like "index" view, we can add more views.

```python
  def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


  def results(request, question_id):
      response = "You're looking at the results of question %s."
      return HttpResponse(response % question_id)


  def vote(request, question_id):
      return HttpResponse("You're voting on question %s." % question_id)
```

From above added views, you can see each function got two arguments "request" and "question_id", "question_id" will fetched desired data from table and it will be defined in the path parameter itself. Let's register URLs for these views as follows.

```python
  urlpatterns = [
      path("admin/", admin.site.urls),
      path("", views.index, name="index"),
      path("<int:question_id>/", views.detail, name="detail"), # new urls
      path("<int:question_id>/results/", views.results, name="results"),
      path("<int:question_id>/vote/", views.vote, name="vote"),
  ]
```

These views can be accessed via URLs:

- Detail View: [http://127.0.0.1:8000/1/](http://127.0.0.1:8000/1/)
- Result view: [http://127.0.0.1:8000/1/results/](http://127.0.0.1:8000/1/results/)
- Vote view: [http://127.0.0.1:8000/1/vote/](http://127.0.0.1:8000/1/vote/)

Easssyyy, let's make views actually do something. Let's make index view list latest 5 question posted and refer below for the code. This will list the latest questions in the index page itself.

```python
  def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])

    return HttpResponse(output)
```

### Django Templates

Django lets you use built-in template system for displaying the data into UI and also can be tweaked as per visual apperance required. Django supports Jinja templates to do so and [click here](https://docs.djangoproject.com/fr/4.2/topics/templates/) to know more.

To render the templates of your application, it needs to be added in application folder with name "templates" since this will let Django know there are templates to load and it will render the each HTML files inside it. Now create template folder inside app(polls) folder and then sub-folder "polls" to make all views that are created belongs to app "polls" and this will avoid future conflict where if two apps has name template name. Folder structure looks as below.

```
mysite
  |-polls
    |-templates
      |-polls
        |-index.html
```

Now add jinja syntax to fetch index data and iterate for each questions.

```html
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}
```

And view know about it where view needs to load the template and replace relevant data in the place holder present in the template as follows below.

```python
  def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # loader will see through template folder and loads asked template
    template = loader.get_template("polls/index.html")

    # making place holder to add the values into templates
    context = {
        "latest_question_list": latest_question_list,
    }

    # HttpResponse will render the relevant data into template
    return HttpResponse(template.render(context, request))
```

Since the loading and rendering takes two steps, we can use shortcuts like "render()" get it done in single step. Follow the code below for it.

```python
  def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # making place holder to add the values into templates
    context = {
        "latest_question_list": latest_question_list,
    }

    # render will directly load and render the relevant data into template
    return render(request, "polls/index.html", context)
```

Now let's add error handling page too, since exception cases are invitable, we need make our application as error proof as possible. Taking an example where we will add exception handling for question ID that doesn't exists for "detail" view.

```python
  def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    # 404 page for not existing data.
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    # rendoring the detail template.
    return render(request, "polls/detail.html", {"question": question})
```

Again Django make it easier, so it's shortcut time. We will use "get_object_or_404" for it and follow the below code for the reference.

```python
  def detail(request, question_id):
    # loads the template if data exists or loads the error template
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {"question": question})
```

Let's update the detail template to display question and choice as bullet point, refer code below for reference.

```html
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }}</li>
  {% endfor %}
</ul>
```

Let's clean up the redirecting URLs or hrefs too, previously we have added href as below follows in polls/index.html file.

```html
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

This is bad coding practice. Infact, hard coding anything is bad coding pratice. Here will take off URLs and just use name that we have given while registering the view's url. For example:

```python
  path("<int:question_id>/", views.detail, name="detail"),
```

So the href in polls/index.html file changes from

```html
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

to this, "detail" is the name that will Django understands which view to trigger when href is clicked.

```html
<li>
  <a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>
</li>
```
