from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.context_processors import auth 


# Create your views here.

@login_required(login_url='myauth:login')
def show_main(request):
    user_data = {
        'user_type': request.user.ajeg_user.user_type
    }
    print(user_data)
    return render(request, 'main.html', user_data)

def landing(request):

    return render(request, 'landing.html')