from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from review.models import *
from main.models import Product
from django.core.serializers import serialize


def render_reviews_panel(request, product_id: int):
    product = Product.objects.get(pk=product_id)
    return render(request, "reviews_panel.html", {"product": product})


def fetch_review_by_id(request: HttpRequest, id: uuid.UUID) -> HttpResponse:
    response = HttpResponse()

    try:
        review = UserReview.objects.get(pk=id)
    except UserReview.DoesNotExist:
        response.content = "The specified review does not exist"
        response.status_code = 404
        return response

    response.content = serialize("json", [review])
    response.status_code = 200
    return response


def fetch_reviews_by_product(request: HttpRequest, product_id: int):
    try:
        product = Product.objects.get(pk=product_id)
        reviews = UserReview.objects.filter(product=product)
    except Product.DoesNotExist or UserReview.DoesNotExist:
        return HttpResponse("Product not found", status=404)

    return HttpResponse(serialize("json", reviews), status=200)


def fetch_reviews_by_store(request: HttpRequest, store_id: int):
    store = Store.objects.get(pk=store_id)
    products = Product.objects.filter(store=store)
    reviews = UserReview.objects.filter(product=products)
    return HttpResponse(serialize("json", reviews), status=200)


def fetch_all_reviews(request) -> HttpResponse:
    reviews = UserReview.objects.all()
    return HttpResponse(serialize("json", reviews), status=200)


@require_POST
def add_comment(request: HttpRequest, id: uuid.UUID) -> HttpResponse:
    """
    Adds a comment to the `UserReview` with the specified ID

    Args
        `id` - The UUID of the specified `UserReview`

    The function expects one argument in the request body:
        `content` - A string containing the contents of the comment

    The function returns
    """
    response = HttpResponse()

    try:
        review = UserReview.objects.get(pk=id)
    except UserReview.DoesNotExist:
        response.content = "The specified review does not exist"
        response.status_code = 404
        return response

    new_comment = Comment(content=request.POST.get("content"), target=review)
    new_comment.save()

    response.content = "The comment was successfully created"
    response.status_code = 200
    return response
