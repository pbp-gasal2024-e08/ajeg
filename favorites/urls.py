from django.urls import path
from favorites.views import view_favorites, favorite_product, favorite_store

app_name = 'favorites'

urlpatterns = [
    path('favorites/', view_favorites, name='favorites'),
    path('favorites/toggle-store', favorite_store, name='toggle_favorite_store'),
    path('favorites/toggle-product',favorite_product, name='toggle_favorite_product'),
]