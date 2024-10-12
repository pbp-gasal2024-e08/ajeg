from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AjegUser(models.Model):
    ajeg_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=[('traveller', 'Traveller'), ('merchant', 'Merchant')], max_length=10)