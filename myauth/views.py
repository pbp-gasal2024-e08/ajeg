from operator import is_
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from myauth.forms import CreateUserForm

# Create your views here.

def register_user(request): 
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form.data)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('myauth:login')
    context = {'form': form}
    return render(request, 'register_user.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('main:show_main')
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, "Invalid username or password. Please try again.")
            return render(request, 'login.html')
    if request.user.is_authenticated:
        return redirect('main:show_main')
    else:
        return render(request, 'login.html')


