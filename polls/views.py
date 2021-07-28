from django.shortcuts import render
from .models import Question, Choice

from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
	questions = Question.objects.order_by('-pub_date')[:6]
	context = {'questions':questions}
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	question = Question.objects.get(id=question_id)
	context = {'question':question}
	return render(request, 'polls/detail.html', context)


def vote(request, question_id):
	question = Question.objects.get(pk=question_id)
	try:
		choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question':question, 
			'error_message': "You didn't select a choice.",
			})
	else:
		choice.votes += 1
		choice.save()
		# context = {'question':question, 'choice':choice}
		# return render(request, 'polls/results.html', context)
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



def results(request, question_id):
	question = Question.objects.get(pk=question_id)
	context = {'question':question}
	return render(request, 'polls/results.html' , context)