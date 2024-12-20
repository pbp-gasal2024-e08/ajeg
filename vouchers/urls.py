from django.urls import path, include
from vouchers import views
from . import views

app_name = "vouchers"

urlpatterns = [
    path("", views.voucher_list, name="voucher_list"),
    # path('vouchers/', include('vouchers.urls')),  # Pastikan ini mengarah ke file urls.py yang benar
    path(
        "claim-voucher/<str:code>/", views.claim_voucher, name="claim_voucher"
    ),
    path("vouchers-json/", views.voucher_list_json, name="voucher_list_json"),
    path("add-to-cart/<str:code>/", views.add_to_cart, name="add_to_cart"),
    # path('remove-from-cart/<str:code>/', views.remove_from_cart, name='remove_from
]
