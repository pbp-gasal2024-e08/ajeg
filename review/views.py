from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


from review.models import *
from django.core.serializers import serialize


def fetch_review(request: HttpRequest, id: uuid.UUID) -> HttpResponse:
    review: UserReview = None
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


def fetch_all_reviews(request) -> HttpResponse:
    reviews = UserReview.objects.all()
    context = {"reviews": reviews}
    return render(request, "test.html", context)


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
    review: UserReview = None
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
