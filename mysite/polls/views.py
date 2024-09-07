from django.http import HttpResponse

# from django.template import loader
from django.shortcuts import render

from polls.models import Question


# Create your views here.

# Without template view
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]

#     output = ", ".join([q.question_text for q in latest_question_list])

#     return HttpResponse(output)


# with template view via loading and rendering
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]

#     # loader will see through template folder and loads asked template
#     template = loader.get_template("polls/index.html")

#     # making place holder to add the values into templates
#     context = {
#         "latest_question_list": latest_question_list,
#     }

#     # HttpResponse will render the relevant data into template
#     return HttpResponse(template.render(context, request))


# with template view via shortcut for loading and rendering
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # making place holder to add the values into templates
    context = {
        "latest_question_list": latest_question_list,
    }

    # render will directly load and render the relevant data into template
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
