from django.urls import path,include

from qa.views import add_question


urlpatterns = [
    path('add_question/', add_question)
]