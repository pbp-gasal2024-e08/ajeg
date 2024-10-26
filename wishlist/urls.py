from django.urls import path
from wishlist.views import view_wishlist, add_to_wishlist, delete_from_wishlist, edit_wishlist

app_name = "wishlist"

urlpatterns = [
    path('wishlist/', view_wishlist, name='wishlist'),
    path('wishlist/delete/<int:product_id>/', delete_from_wishlist, name='delete_wishlist_item'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_wishlist_item'),
    path('wishlist/edit/<int:product_id>/', edit_wishlist, name='edit_wishlist_item'),
]