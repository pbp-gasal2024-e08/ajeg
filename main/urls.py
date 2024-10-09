from django.urls import path
from main.views import show_main

app_name = "main"

urlpatterns = [
    path("landing/", show_main, name="landing"),
]