from django.urls import path

from review.views import *

urlpatterns = [
    path("product/<int:product_id>", render_reviews_panel, name="render_reviews_panel"),
    path("", fetch_all_reviews, name="fetch_all_reviews"),
    path("<uuid:id>", fetch_review_by_id, name="fetch_review"),
    path(
        "by-product/<int:product_id>",
        fetch_reviews_by_product,
        name="fetch_reviews_by_product",
    ),
    path(
        "by-store/<int:store_id>", fetch_reviews_by_store, name="fetch_reviews_by_store"
    ),
    path("add-review/<int:product_id>", add_review, name="add_review"),
    path("edit-review/<uuid:id>", edit_review_by_id, name="edit_review_by_id"),
    path("delete-review/", delete_review_by_id, name="delete_review_by_id"),
    path("add-comment/<uuid:id>", add_comment, name="add_comment"),
    # URL to check if user is authenticated
    path("check", check, name="check"),
]
