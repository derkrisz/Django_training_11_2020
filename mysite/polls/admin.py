from django.contrib import admin
from .models import Question, Choice
# Register your models here.


# we can combine models
class ChoiceInLine(admin.StackedInline):
    model = Choice
    # let's allow additional choices
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),('Date', {'fields':['pub_date']})]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
