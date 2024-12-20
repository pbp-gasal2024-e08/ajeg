from django.urls import path
from main.views import show_main, landing, myprofile_page, store_page

app_name = "main"

urlpatterns = [
    path("", landing, name="landing"),
    path("home/", show_main, name="show_main"),
    path("myprofile/", myprofile_page, name="myprofile_page"),
    path("mystore/", store_page, name="mystore_page"),
]
