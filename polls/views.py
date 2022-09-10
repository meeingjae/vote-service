from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

# Create your views here.
from .models import Question


def custom_index_v1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def custom_index_v2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))


def custom_index_v3(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("this is parameter question_id : %s" % question_id)


def detail_v2_not_found(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def detail_v3_not_found(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'quetion': question})


def results(request, question_id):
    return HttpResponse("result of question. question_id : %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you are vote question %s." % question_id)
