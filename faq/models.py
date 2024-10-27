import uuid
from django.db import models
from django.contrib.auth.models import User
from main.models import Product

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # product_asked = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=169)
    question = models.TextField()
    answer = models.TextField(default="")

# class Answer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.OneToOneField(Question, on_delete=models.CASCADE)
#     answer = models.TextField()