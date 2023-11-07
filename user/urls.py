from django.urls import path
from user.views import register_account


urlpatterns = [
    path('register-account/', register_account)
]