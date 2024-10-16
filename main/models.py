from django.db import models

# Create your models here.

class Toko(models.Model):
    nama_toko = models.CharField(max_length=255)
    url = models.URLField()
    range_harga = models.CharField(max_length=10)
    rating = models.FloatField()
    kategori = models.JSONField()

    def __str__(self):
        return self.nama_toko

class Product(models.Model):
    toko = models.ForeignKey(Toko, related_name='products', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama
