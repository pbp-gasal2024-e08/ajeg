from django.urls import path
from main.views import show_main, landing

app_name = "main"

urlpatterns = [
    path("", landing, name="landing"),
    path("home/", show_main, name="show_main"),
]