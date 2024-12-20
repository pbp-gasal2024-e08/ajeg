from django.urls import path
from mobile_auth.views import login, register

app_name = "mobile_auth"

urlpatterns = [
    path("mobile-login/", login, name="mobile_login"),
    path("mobile-register/", register, name="mobile_register"),
]
