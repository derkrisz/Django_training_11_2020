from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse # reverse url lookup can read a route
# Create your views here.
def index(request): # a functional view, receiving the entire request the user made
    question_list = Question.objects.order_by('-pub_date')[:10] # pylint: disable=maybe-no-member
    #output = ', '.join([q.question_text for q in question_list]) # this is a comprehension
    # use a template to iterate over them
    #template = loader.get_template('polls/index.html') #we do not need this explicitly
    context = {'question_list':question_list}
    # we return something for the user to see
    #return HttpResponse(template.render(context, request))
    return HttpResponse(render(request, 'polls/index.html', context))

def detail(request, question_id):
    #try:
        # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    #except Question.DoesNotExist:
     #   raise Http404('Question does not exist')
    #response = f'This is question number {question_id}'
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    #response = f'Results for question number {question_id}'
    #return HttpResponse(response)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        #just show the form again
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Invalid choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

