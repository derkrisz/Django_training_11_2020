from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question, Choice

class QuestionModelTests(TestCase):
    ''' We should write a docstring '''
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=12)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_published_with_an_old_question(self):
        ''' desc here '''
        time = timezone.now() - datetime.timedelta(days=-3)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)
    
    def test_published_today(self):
        today = timezone.now() - datetime.timedelta(days=0, seconds=88)
        todays_question = Question(pub_date=today)
        self.assertIs(todays_question.was_published_recently(), True)


class ChoiceModelTests(TestCase):
    def test_choice_text(self):
        choice = Choice(choice_text='sometext')
        self.assertEqual(choice.choice_text, 'sometext')

    def test_choice_vote(self):
        choice = Choice(choice_text='example', votes=3)
        self.assertEqual(choice.votes, 3)
    
    def test_default_vote(self):
        choice = Choice(choice_text='test')
        self.assertEqual(choice.votes, 0)


# to run
# manage.py test polls