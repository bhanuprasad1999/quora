from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate, login

from user.forms import LoginForm
# Create your views here.
  
def register_account(request):  
    form = UserCreationForm(request.POST)
    print(form)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
        return redirect('/qa/add_question/')
    else:  
        form = UserCreationForm()

    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)


def loggin_account(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            return redirect('/qa/add_question/')
        else:
            form = LoginForm()
    else:
        form = LoginForm()
    context = {
        'form':form
    }
    return render(request, 'login.html', context=context)