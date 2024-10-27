from django.urls import path
from favorites.views import view_favorites, favorite_product, favorite_store, get_favorite_item_ids, get_favorite_store_ids

app_name = 'favorites'

urlpatterns = [
    path('favorites/', view_favorites, name='favorites'),
    path('favorites/toggle-store', favorite_store, name='toggle_favorite_store'),
    path('favorites/toggle-product',favorite_product, name='toggle_favorite_product'),
    path('favorites/get-favorite-ids', get_favorite_item_ids, name='get_favorite_ids'),
    path('favorites/get-favorite-store-ids', get_favorite_store_ids, name='get_favorite_store_ids')
]