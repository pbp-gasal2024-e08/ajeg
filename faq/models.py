from django.db import models
from django.contrib.auth.models import User
from main.models import Product

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_asked = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=169)
    question = models.TextField()
    answered = models.BooleanField(default=False)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.TextField()