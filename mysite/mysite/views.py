from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request): # a functional view, receiving the entire request the user made
    # we return something for the user to see
    return HttpResponse('Root index page')