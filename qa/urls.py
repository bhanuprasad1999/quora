from django.urls import path,include

from qa.views import add_question, submit_answer_for_question, view_question_and_answer, list_questions


urlpatterns = [
    path('add_question/', add_question, name='add_question'), 
    path('view_question/<int:id>', view_question_and_answer, name='view_question'),
    path('submit_your_answers/<int:question_id>', submit_answer_for_question, name='submit_answer_for_question'),
    path('question_list/', list_questions, name='list_questions')
]