from django.urls import path
from checkout.views import show_cart, show_checkout, show_order_summary, show_product_page, show_order_confirmation

app_name = 'checkout'

urlpatterns = [
    path('checkout/', show_checkout, name='show_checkout'),
    path('cart/', show_cart, name='show_cart'),
    path('order_summary/', show_order_summary, name='show_order_summary'),
    path('product_page/<int:pk>/', show_product_page, name='show_product_page'),
    path('order_confirmation/', show_order_confirmation, name='show_order_confirmation'),
]