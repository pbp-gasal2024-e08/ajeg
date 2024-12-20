import uuid

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt

from myauth.models import AjegUser
from review.models import UserReview, Comment
from main.models import Product, Store
from django.core.serializers import serialize

# TODO: MAKE SURE TO UPDATE THIS FILE IF ID TYPE BECOMES CHANGED TO UUID


def render_reviews_panel(request, product_id: int):
    product = get_object_or_404(Product, pk=product_id)

    user = None
    if request.user.is_authenticated:
        user = AjegUser.objects.get(ajeg_user=request.user)

    return render(request, "reviews_panel.html", {"product": product, "user": user})


def fetch_review_by_id(request: HttpRequest, id: uuid.UUID) -> HttpResponse:
    review = get_object_or_404(UserReview, id=id)

    return JsonResponse(review.serialize(), status=200)


def fetch_reviews_by_product(request: HttpRequest, product_id: int):
    product = get_object_or_404(Product, pk=product_id)
    reviews = UserReview.objects.filter(product=product)

    reviews_json = []
    for review in reviews:
        review_json = review.serialize()
        if review.creator == request.user.ajeg_user:
            review_json["editable"] = True
        else:
            review_json["editable"] = False
        reviews_json.append(review_json)

    return JsonResponse(reviews_json, safe=False, status=200)


# Check this implementation in the future
def fetch_reviews_by_store(request: HttpRequest, store_id: int):
    store = get_object_or_404(Store, pk=store_id)
    products = Product.objects.filter(store=store)

    # "Initialize" an empty queryset with a plain UserReview manager
    all_reviews = UserReview.objects.none()
    # Merge the separate querysets into one large queryset
    for product in products:
        all_reviews = all_reviews | UserReview.objects.filter(product=product)
    return HttpResponse(
        serialize("json", all_reviews),
        status=200,
    )


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
    product = get_object_or_404(Product, pk=product_id)

    creator: AjegUser = request.user.ajeg_user

    # TODO: Check if user has bought this product

    star_rating = request.POST.get("star_rating")

    review = UserReview.objects.create_review(
        creator=creator,
        product=product,
        synopsis=request.POST.get("synopsis"),
        star_rating=star_rating,
        base_comment=request.POST.get("base_comment"),
    )

    product.review_count += 1

    # Calculate new average rating of product
    product.average_rating = (
        product.average_rating * (product.review_count - 1) + int(star_rating)
    ) / product.review_count

    product.save()

    return HttpResponse(serialize("json", [review]), status=201)


@login_required(login_url="/login")
def edit_review_by_id(request: HttpRequest, id: uuid.UUID):
    review = get_object_or_404(UserReview, id=id)

    new_star_rating = request.POST.get("star_rating")

    product = review.product

    # Recalculate new average rating for product
    total_prod = product.average_rating * product.review_count
    product.average_rating = (
        total_prod - review.star_rating + new_star_rating
    ) / product.review_count

    product.save()

    review.star_rating = new_star_rating
    review.synopsis = request.POST.get("synopsis")
    review.base_comment.content = request.POST.get("base_comment")

    review.save()
    review.base_comment.save()  # make sure to also save the referenced object :')

    return HttpResponse("Review successfully edited!", status=200)


@login_required(login_url="/login")
@require_POST
@csrf_exempt
def delete_review_by_id(request: HttpRequest):
    try:
        review = UserReview.objects.get(id=request.body.decode(encoding="utf-8"))
    except UserReview.DoesNotExist:
        return HttpResponse("Review does not exist!", status=204)

    if review.creator != request.user.ajeg_user:
        return HttpResponse("You are not the creator of this review!", status=403)

    product = review.product

    # Recalculate new average product rating
    product.review_count -= 1
    product.average_rating = (
        product.average_rating * (product.review_count + 1) - review.star_rating
    ) / product.review_count

    product.save()

    review.delete()

    return HttpResponse("Review successfully deleted!", status=200)


@login_required(login_url="/login")
@require_POST
def add_comment(request: HttpRequest, id: uuid.UUID) -> HttpResponse:
    """
    Adds a comment to the `Comment` with the specified ID

    Args
        `id` - The ID of the specified target `Comment`

    The function expects one argument in the request body:
        `content` - A string containing the contents of the comment
    """
    target_comment = get_object_or_404(Comment, pk=id)

    # TODO: Fix the logic here, it's broken ATM
    creator: AjegUser = request.user.ajeg_user
    new_comment = Comment.objects.create(
        creator=creator,
        content=request.POST.get("content"),
        target=target_comment,
    )

    return HttpResponse("The comment was successfully created", status=200)


@login_required(login_url="/login")
def check(request):
    """
    Helper view function to check if user is logged_in asynchronously
    """
    return HttpResponse(request.user, status=200)
