from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import datetime
from django.shortcuts import render, redirect

from myauth.forms import CreateUserForm, CreateStoreForm


# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("myauth:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect("main:show_main")
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.info(
                request, "Invalid username or password. Please try again."
            )
            return render(request, "login.html")
    if request.user.is_authenticated:
        return redirect("main:show_main")
    else:
        return render(request, "login.html")


def logout_user(request):
    logout(request)
    response = redirect("main:landing")
    response.delete_cookie("last_login")
    return response
