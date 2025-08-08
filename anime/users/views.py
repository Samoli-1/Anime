from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .form import Authentication

def SignUp(request):
    if request.method == 'POST':
        login_form = Authentication(request.POST)
        if(login_form.is_valid()):
            login_form.save()
            return redirect('users:login')
    else:
        login_form = Authentication()
    return render(request, 'users/signup.html', {'form':login_form})


def Logout(request):
    logout(request)
    return redirect('home:index')