from django.urls import path
from main.views import show_main, landing, myprofile_page, store_page, get_products, get_product_by_id

app_name = "main"

urlpatterns = [
    path("", landing, name="landing"),
    path("home/", show_main, name="show_main"),
    path("myprofile/", myprofile_page, name="myprofile_page"),
    path("mystore/", store_page, name="mystore_page"),
    path("get-products/", get_products, name="get_products"),
    path("get-product/", get_product_by_id, name="get_product_by_id"),
]
