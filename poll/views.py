from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from .models import Question


# Create your views here.
def index(request):
    latest_question = Question.objects.order_by('-pub_text')[:5]
    # output = ', '.join([q.question_text for q in latest_question])
    # template = loader.get_template('poll/index.html')
    context = {'latest_question': latest_question, }
    return render(request, 'poll/index.html', context)


# get questions and display
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})


def results(request, question_id):
    response = "This is a result for question % s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("This is a vote for question %s." % question_id)
