from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.context_processors import auth 

from main.models import Product
from announcement.models import Announcement

# Create your views here.

@login_required(login_url='myauth:login')
def show_main(request):
    user_data = {
        'user_type': request.user.ajeg_user.user_type
    }
    context= {
        'user_data': user_data, 
        'products': Product.objects.all(),
        }
    return render(request, 'main.html', context)

def landing(request):

    return render(request, 'landing.html')