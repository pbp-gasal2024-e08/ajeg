from django.db import models
from django.contrib.auth.models import User
from main.models import Store, Product

# Create your models here.
class FavoriteStoreList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite_store_list")

class FavoriteStore(models.Model):
    favorite_list = models.ForeignKey(FavoriteStoreList, on_delete=models.CASCADE, related_name="items")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

class FavoriteProductList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite_product_list")

class FavoriteProduct(models.Model):
    favorite_list = models.ForeignKey(FavoriteProductList, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)