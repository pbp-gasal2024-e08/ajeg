from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.context_processors import auth
from django.core import serializers

from main.models import Product, Store
from announcement.models import Announcement

# Create your views here.


def landing(request):
    return render(request, "landing.html")

@login_required(login_url="myauth:login")
def show_main(request):
    user_data = {"user_type": request.user.ajeg_user.user_type}
    context = {
        "user_data": user_data,
        "products": Product.objects.all(),
    }
    return render(request, "main.html", context)


@login_required(login_url="myauth:login")
def myprofile_page(request):
    user = request.user.ajeg_user

    context = {"user": user}
    return render(request, "myprofile_page.html", context)

@login_required(login_url="myauth:login")
def store_page(request):
    return render(request, "store_page.html")

def get_products(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
