from django.urls import path
from myauth.views import register, login_user

app_name = 'auth'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
]