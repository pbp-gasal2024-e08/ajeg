from django.contrib import admin

# Register your models here.
from wishlist.models import Wishlist, WishlistItem

admin.site.register(WishlistItem)
admin.site.register(Wishlist)