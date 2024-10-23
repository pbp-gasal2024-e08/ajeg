from django.urls import path

from review.views import *

urlpatterns = [
    path("", fetch_all_reviews, name="fetch_all_reviews"),
    path("<uuid:id>", fetch_review, name="fetch_review"),
    path("add_comment/<uuid:id>", add_comment, name="add_comment"),
]
