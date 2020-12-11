from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic    # these are generic view classes we can extend

from .models import Choice, Question
from .name_form import NameForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html' #default would be polls/question_list.html
    #context_object_name = 'question_list' #question_list is default which is what I use in the template.

    def get_queryset(self):
        """Return the last ten published questions."""
        return Question.objects.order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    model = Question    # the exact question would be derived from pk parameter
    template_name = 'polls/detail.html'     # default would be polls/question_detail.html

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class ChildView(generic.ListView):
    model = Question
    template_name = 'polls/child.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:10]
    

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

# here is a view which handles getting the user name from a form called NameForm

def get_name(request):
    if request.method == 'POST':
        name_form = NameForm(request.POST)
        if name_form.is_valid():
            subject = name_form.cleaned_data['subject']
            message = name_form.cleaned_data['message']
            sender = name_form.cleaned_data['sender']
            cc_myself = name_form.cleaned_data['cc_myself']
            return HttpResponse(f'Thank you for the data {subject}, {message}, {sender}, {cc_myself}')
    else:
        name_form = NameForm()
        return render(request, 'polls/name_form.html', {'name_form':name_form})
