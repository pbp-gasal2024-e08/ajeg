"""
This package contains two models:
    1. `UserReview` - A single review by a user
    2. `Comment` - A comment that can be given to another `Comment` object
"""

import uuid
from django.db import models
from main.models import Product
from myauth.models import AjegUser


class UserReviewManager(models.Manager):
    def create_review(
        self,
        creator: AjegUser,
        product: Product,
        synopsis: str,
        star_rating: int,
        base_comment: str,
    ):
        base_comment = Comment.objects.create(content=base_comment, target=None)
        review = self.create(
            creator=creator,
            product=product,
            synopsis=synopsis,
            star_rating=star_rating,
            base_comment=base_comment,
        )

        return review


class Comment(models.Model):
    """
    Comments given to another `Comment` object.

    A `UserReview` has one `base_comment`, which is a `Comment` object that can
    be referenced by another `Comment`, effectively acting as a reply to said comment
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=1000, null=False, blank=False)
    creator = models.ForeignKey(AjegUser, null=True, on_delete=models.SET_NULL)
    target = models.ForeignKey("self", null=True, on_delete=models.CASCADE)


class UserReview(models.Model):
    """
    Reviews given to a product by a user

    A `UserReview` needs a base comment in order for other comments to latch onto it.

    Create a `UserReview` object using the `UserReview.objects.create_review(creator, product, star_rating, base_comment)` helper method.
    """

    objects = UserReviewManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(AjegUser, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Make sure a star rating is given for each review
    star_rating = models.PositiveSmallIntegerField(null=False, blank=False)
    synopsis = models.CharField(max_length=50, null=True, blank=True)
    base_comment = models.OneToOneField(Comment, on_delete=models.CASCADE, null=False)

    # TODO: Add image upload field
    def serialize(self):
        return {
            "id": self.id,
            "product": self.product.id,
            "creator": self.creator.ajeg_user.username,
            "star_rating": self.star_rating,
            "synopsis": self.synopsis,
            "created_at": self.created_at,
            "last_updated": self.last_updated,
            "base_comment": {
                "id": self.base_comment.id,
                "content": self.base_comment.content,
                # "created_at": self.base_comment.created_at,
                # "updated_at": self.base_comment.updated_at,
            },
        }
