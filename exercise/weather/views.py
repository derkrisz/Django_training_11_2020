from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic    # these are generic view classes we can extend

from .models import Weather

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'weather/index.html'

    def get_queryset(self):
        # pylint: disable=maybe-no-member
        return Weather.objects.all()

class DetailView(generic.DetailView):
    model = Weather
    template_name = 'weather/detail.html'