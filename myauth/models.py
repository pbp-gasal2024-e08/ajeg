from django.db import models
from django.contrib.auth.models import User

from main.models import Product, Store


# Create your models here.
class AjegUser(models.Model):
    ajeg_user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="ajeg_user"
    )
    user_type = models.CharField(
        choices=[("traveller", "Traveller"), ("merchant", "Merchant")],
        max_length=10,
    )
    store = models.ManyToManyField(Store, blank=True)

    @property
    def merchant_store(self):
        if self.user_type == "merchant":
            return self.store.all()
        return []

    def add_toko(self, value):
        if self.user_type == "merchant":
            self.store.add(value)

    def __str__(self):
        return self.ajeg_user.username


class StoreUserRelation(models.Model):
    user = models.ForeignKey(
        AjegUser, on_delete=models.CASCADE, related_name="userstore"
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="userstore")
