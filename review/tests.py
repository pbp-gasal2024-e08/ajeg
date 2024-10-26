from django.test import TestCase

from django.contrib.auth.models import User
from myauth.models import AjegUser
from main.models import Store, Product, Category
from review.models import UserReview, Comment


class ReviewTest(TestCase):
    def setUp(self):
        a = User.objects.create(username="Alice", password="12345678")
        b = User.objects.create(username="Bob", password="87654321")
        self.alice = AjegUser.objects.create(ajeg_user=a, user_type="traveller")
        self.bob = AjegUser.objects.create(ajeg_user=b, user_type="traveller")
        self.store = Store.objects.create(
            name="ajeg_store", url="www.ajeg.com", price_range="$$$", rating=0.0
        )
        self.product = Product.objects.create(
            store=self.store,
            name="product1",
            price=20000,
            description="Here's a description",
        )

    def test_create_review(self):
        review = UserReview.objects.create_review(
            creator=self.alice,
            product=self.product,
            star_rating=5,
            base_comment="Great store!",
        )
        self.assertIsNotNone(review.id)
        self.assertEqual(review.creator, self.alice)
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.star_rating, 5)
        self.assertEqual(review.base_comment.content, "Great store!")


class CommentTest(TestCase):
    pass


class IntegratedTest(TestCase):
    pass
