"""
This package contains two models:
    1. `UserReview` - A single review by a user
    2. `Comment` - A comment that can be given to a `UserReview` or `StoreReview`
"""

import uuid
from django.db import models
from main.models import Product, Store


class UserReview(models.Model):
    """
    Reviews given to a product by a user
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Make sure a star rating is given for each review
    star_rating = models.PositiveSmallIntegerField(null=False, blank=False)

    # TODO: Add image upload field


class Comment(models.Model):
    """
    Comments given to a UserReview
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=1000, null=False, blank=False)
    target = models.ForeignKey(UserReview, null=False, on_delete=models.CASCADE)


class Reply(models.Model):
    """
    Replies given to a Comment
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=1000, null=False, blank=False)
    target = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE)
