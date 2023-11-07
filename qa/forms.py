from forms import ModelForms
from qa.models import Answers, Questions, Ratings



class QuestionForm(ModelForms):
    class Meta:
        model = Questions
        fields = ['question_title', 'question_description']


class AnswerForm(ModelForms):
    class Meta:
        model = Answers
        fields = ['answer']


class RatingForm(ModelForms):
    class Meta:
        model = Ratings
        fields = ['vote']