from django.urls import path
from myauth.views import register
from myauth.views import login_user, logout_user

app_name = 'myauth'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]