# this is not normal production - just for demo purposes
from django.utils import timezone

from polls.models import Choice, Question


# see all the Question modelss
print(Question.objects.all())

q = Question(question_text='Is it lunch yet?', pub_date=timezone.now())
q.save()

print(q.id, q.question_text, q.pub_date)

question_text = 'Not yet lunch is it?'
print(q.id, q.question_text, q.pub_date)

print(Question.objects.all())