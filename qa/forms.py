from django.forms import ModelForm
from qa.models import Answers, Questions, Ratings



class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question_title', 'question_description']


class AnswerForm(ModelForm):
    class Meta:
        model = Answers
        fields = ['answer']
