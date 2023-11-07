from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  
# Create your views here.
  
def register_account(request):  
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/qa/add_question/')
    else:  
        form = UserCreationForm()

    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)