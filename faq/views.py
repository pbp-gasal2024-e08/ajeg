from django.shortcuts import render
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST
from faq.forms import QuestionForm
from faq.models import Question
from main.models import Product
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json


@login_required(login_url="/login")
def view_faq(request):
    context = {}
    return render(request, "view_faq.html", context)


def show_json(request):
    data = Question.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


@csrf_exempt
@require_POST
def add_question_ajax(request):
    user = request.user
    title = strip_tags(request.POST.get("title"))
    question = strip_tags(request.POST.get("question"))
    # product_asked = Product.objects.get(pk=request.POST.get("id"))
    new_question = Question(
        user=user,
        # product_asked=product_asked,
        title=title,
        question=question,
    )
    new_question.save()
    return HttpResponse(b"CREATED", status=201)


@csrf_exempt
@require_POST
def add_answer_ajax(request, id):
    question = Question.objects.get(pk=id)
    answer = request.POST.get("answer")
    question.answer = answer
    question.save()
    return HttpResponse(b"CREATED", status=201)
