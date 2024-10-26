import uuid

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from myauth.models import AjegUser
from review.models import UserReview, Comment
from main.models import Product, Store
from django.core.serializers import serialize

# TODO: MAKE SURE TO UPDATE THIS FILE IF ID TYPE BECOMES CHANGED TO UUID


def render_reviews_panel(request, product_id: int):
    product = Product.objects.get(pk=product_id)

    user = None
    if request.user.is_authenticated:
        user = AjegUser.objects.get(ajeg_user=request.user)

    return render(request, "reviews_panel.html", {"product": product, "user": user})


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

    reviews_json = []
    for review in reviews:
        reviews_json.append(review.serialize())

    return JsonResponse(reviews_json, safe=False, status=200)


# Check this implementation in the future
def fetch_reviews_by_store(request: HttpRequest, store_id: int):
    store = Store.objects.get(pk=store_id)
    products = Product.objects.filter(store=store)
    reviews = UserReview.objects.filter(product=products)
    return HttpResponse(serialize("json", reviews), status=200)


def fetch_all_reviews(request) -> HttpResponse:
    reviews = UserReview.objects.all()
    return HttpResponse(serialize("json", reviews), status=200)


@login_required(login_url="/login")
@require_POST
def add_review(request: HttpRequest, product_id: int):
    """
    Adds a review to the `Product` with the specified ID

    Args
        `id` = The ID of the specified `Product`

    The function expects two arguments in the request body:
        `star_rating` - An integer between 1 and 5 representing the star rating given to the product
        `comment` - An optional comment left along with the star rating
    """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponse("This product wasn't found!", status=404)

    creator: AjegUser = request.user.ajeg_user

    # TODO: Check if user has bought this product

    review = UserReview.objects.create_review(
        creator=creator,
        product=product,
        star_rating=request.POST.get("star_rating"),
        base_comment=request.POST.get("base_comment"),
    )

    return HttpResponse(serialize("json", [review]), status=201)


@require_POST
def add_comment(request: HttpRequest, id: uuid.UUID) -> HttpResponse:
    """
    Adds a comment to the `Comment` with the specified ID

    Args
        `id` - The ID of the specified target `Comment`

    The function expects one argument in the request body:
        `content` - A string containing the contents of the comment
    """
    response = HttpResponse()

    try:
        target_comment = Comment.objects.get(pk=id)
    except UserReview.DoesNotExist:
        response.content = "The specified review does not exist"
        response.status_code = 404
        return response

    # TODO: Fix the logic here, it's broken ATM
    creator: AjegUser = request.user.ajeg_user
    new_comment = Comment(
        creator=creator, content=request.POST.get("content"), target=target_comment
    )
    new_comment.save()

    response.content = "The comment was successfully created"
    response.status_code = 200
    return response


@login_required(login_url="/login")
def check(request):
    """
    Helper view function to check if user is logged_in asynchronously
    """
    return HttpResponse(request.user, status=200)
