# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.views import generic
from django.views.decorators.cache import cache_page

from .forms import AddForm
from .models import Question, Choice


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            template_name='polls/detail.html',
            context={'error_message': "You didn't select a choice.", "question": question}
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))


def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    result = str(int(a) + int(b))
    return HttpResponse(result)


@cache_page(60 * 2)
def home(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
        else:
            form = AddForm()
    else:
        form = AddForm()
    return render(request, template_name='polls/home.html', context={'form': form})
