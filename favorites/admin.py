from django.contrib import admin

# Register your models here.
from favorites.models import FavoriteStoreList, FavoriteStore, FavoriteProductList, FavoriteProduct

admin.site.register(FavoriteStoreList)
admin.site.register(FavoriteStore)
admin.site.register(FavoriteProductList)
admin.site.register(FavoriteProduct)