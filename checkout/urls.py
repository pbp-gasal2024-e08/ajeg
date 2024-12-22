from django.urls import path
from requests import delete
from .views import (
    show_cart,
    show_checkout,
    show_order_summary,
    show_product_page,
    show_order_confirmation,
)
from .views import (
    get_cart_json,
    update_cart_quantity,
    get_product_json,
    show_history,
    delete_cart,
)
from .views import store_page

app_name = "checkout"

urlpatterns = [
    path("checkout/", show_checkout, name="show_checkout"),
    path("cart/", show_cart, name="show_cart"),
    path("order-summary/", show_order_summary, name="show_order_summary"),
    path("product-page/<int:pk>/", show_product_page, name="show_product_page"),
    path(
        "order-confirmation/",
        show_order_confirmation,
        name="show_order_confirmation",
    ),
    path("delete-cart/", delete_cart, name="delete_cart"),
    path("get-cart/", get_cart_json, name="get_cart_json"),
    path("get-product/<int:pk>", get_product_json, name="get_product_json"),
    path(
        "update-cart-quantity/",
        update_cart_quantity,
        name="update_cart_quantity",
    ),
    path("store/<int:pk>/", store_page, name="store_page"),
    path("history/", show_history, name="show_history"),
]
