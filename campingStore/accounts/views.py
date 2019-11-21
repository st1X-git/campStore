from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import *

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password', 'default value')

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            # return redirect (request, 'login.html')
            return redirect ('login')

            # return redirect("Invalid login details given")

    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST.get('password1', 'default value')
        password2 = request.POST.get('password2', 'default value')
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken ')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken ")
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, last_name = last_name, first_name = first_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matching.. ')
            return redirect('register')
        return redirect ('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
