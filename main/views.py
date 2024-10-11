from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from myauth.views import login_user

# Create your views here.
@login_required(login_url='myauth:login')
def show_main(request):

    return render(request, 'landing.html')