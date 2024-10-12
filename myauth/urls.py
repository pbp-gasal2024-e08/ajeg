from django.urls import path
from myauth.views import register_user, login_user, logout_user

app_name = 'myauth'

urlpatterns = [
    path('register/user', register_user, name='register_user'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]