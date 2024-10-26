from django.urls import path
from . import views

app_name = 'vouchers'

urlpatterns = [
    path('', views.voucher_list, name='voucher_list'),
    path('claim-voucher/<str:code>/', views.claim_voucher, name='claim_voucher'),
    path('vouchers-json/', views.voucher_list_json, name='voucher_list_json'),
]
