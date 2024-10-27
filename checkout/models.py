from django.db import models

from myauth.models import AjegUser
from main.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(AjegUser, on_delete=models.CASCADE, blank=True, null=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1, blank=True)
    total_price = models.PositiveIntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return str(self.product)