from django.urls import path
from user.views import loggin_account, logout_account, register_account


urlpatterns = [
    path('register-account/', register_account, name='register-account'),
    path('login/', loggin_account, name='login'),
    path('logout/', logout_account, name='logout')
]