from django.urls import path
from main.views import show_main, landing

app_name = "main"

urlpatterns = [
    path("home/", show_main, name="show_main"),
    path("", landing, name="landing"),
]