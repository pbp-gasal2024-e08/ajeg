from django.db import models
import uuid
from main.models import Store


# Create your models here.
class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
