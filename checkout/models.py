from itertools import product
from django.db import models

from myauth.models import AjegUser
from main.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(AjegUser, on_delete=models.CASCADE, blank=True, null=True)
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, blank=True, null=True
    )
    quantity = models.PositiveIntegerField(default=1, blank=True)
    total_price = models.PositiveIntegerField(default=1, blank=True, null=True)
    payment = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "product": self.product.name,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "payment": self.payment,
        }

    def __str__(self):
        return str(self.product)


class Order(models.Model):
    user = models.ForeignKey(AjegUser, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    date = models.DateTimeField()
