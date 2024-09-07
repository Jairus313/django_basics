from django.http import HttpResponse
from django.template import loader

from polls.models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # output = ", ".join([q.question_text for q in latest_question_list])

    # return HttpResponse(output)

    # loader will see through template folder and loads asked template
    template = loader.get_template("polls/index.html")

    # making place holder to add the values into templates
    context = {
        "latest_question_list": latest_question_list,
    }

    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
