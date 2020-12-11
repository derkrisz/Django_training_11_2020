from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse

setup_test_environment()

client = Client() # this emulates client

response = client.get('/nonsuch')

print(response.status_code) # expect 404

response = client.get(reverse('polls:index'))

print(response.status_code) # expect 200
print(response.content) # expect the page
print(response.context['question_list']) # expect the question list

