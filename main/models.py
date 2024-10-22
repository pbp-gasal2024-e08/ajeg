from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)

class Store(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    price_range = models.CharField(max_length=10)
    rating = models.FloatField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Product(models.Model):
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=255, default='produk')
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    description = models.TextField(default='Deskripsi Kosong')

    def __str__(self):
        return self.name

