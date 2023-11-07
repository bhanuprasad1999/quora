from django.urls import path,include

from qa.views import add_question, submit_answer_for_question, update_question, view_question_and_answer, list_questions, vote_for_question, vote_for_answer


urlpatterns = [
    path('add_question/', add_question, name='add_question'),
    path('update_question/<int:question_id>', update_question, name='update_question'),
    path('view_question/<int:id>', view_question_and_answer, name='view_question'),
    path('submit_your_answers/<int:question_id>', submit_answer_for_question, name='submit_answer_for_question'),
    path('question_list/', list_questions, name='list_questions'), 
    path('vote/question/<int:question_id>', vote_for_question, name='vote_for_question'),
    path('vote/answer/<int:answer_id>', vote_for_answer, name='vote_for_answer')
]