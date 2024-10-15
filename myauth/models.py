from django.db import models
from django.contrib.auth.models import User

from main.models import Toko

# Create your models here.
class AjegUser(models.Model):
    ajeg_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ajeg_user')
    user_type = models.CharField(choices=[('traveller', 'Traveller'), ('merchant', 'Merchant')], max_length=10)
    _toko = models.ManyToManyField(Toko, blank=True)

    @property
    def toko(self):
        if self.user_type == 'merchant':
            return self._toko.all()
        return []
    
    @toko.setter
    def toko(self, value):
        if self.user_type == 'merchant':
            self._toko.set(value)

    def __str__(self):
        return self.ajeg_user.username