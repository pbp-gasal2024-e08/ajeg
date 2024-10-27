import datetime
from math import floor
from pickle import FALSE
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from checkout.forms import AddToCartForm
from checkout.models import Cart
from main.models import Product, Store
from myauth.models import AjegUser

import json


# Create your views here.
def show_product_page(request, pk):
    product = Product.objects.get(pk=pk)
    store = Store.objects.get(pk=product.store_id)
    user = AjegUser.objects.get(ajeg_user=request.user)

    form = AddToCartForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        if Cart.objects.filter(user=user, product=product).exists():
            cart = Cart.objects.get(user=user, product=product)
            cart.quantity += form.cleaned_data["quantity"]
            cart.total_price += product.price * form.cleaned_data["quantity"]
            cart.save()
        else:
            cart = Cart.objects.create(
                user=user,
                product=product,
                quantity=form.cleaned_data["quantity"],
                total_price=product.price * form.cleaned_data["quantity"],
            )

    context = {
        "product": product,
        "average_rating": product.average_rating,
        "no_reviews": product.review_count,
        "store": store,
        "form": form,
    }
    return render(request, "product_page.html", context)


@csrf_exempt
@login_required
def show_cart(request):
    carts = Cart.objects.filter(user = request.user.ajeg_user, payment = False)
    context = {
        'carts': carts
    }
    return render(request, 'cart_copy.html', context)

@login_required
def show_history(request):
    carts = Cart.objects.filter(user = request.user.ajeg_user, payment = True)
    context = {
        'carts': carts
    }
    return render(request, 'history.html', context)


@login_required
def show_checkout(request):
    carts = Cart.objects.filter(user=request.user.ajeg_user)

    total_summary = 0
    for cart in carts:
        total_summary += cart.total_price

    tax = int(floor(total_summary * 0.1))
    grand_total = total_summary + tax + 15000

    context = {
        "carts": carts,
        "total_summary": total_summary,
        "tax": tax,
        "grand_total": grand_total,
        "user": request.user,
    }
    return render(request, "checkout.html", context)


@login_required
def show_order_summary(request):
    carts = Cart.objects.filter(user=request.user.ajeg_user)

    total_summary = 0

    for cart in carts:
        total_summary += cart.total_price

    tax = int(floor(total_summary * 0.1))
    grand_total = total_summary + tax
    context = {
        "carts": carts,
        "total_summary": total_summary,
        "tax": tax,
        "grand_total": grand_total,
    }
    return render(request, "order_summary.html", context)


@login_required
def show_order_confirmation(request):
    carts = Cart.objects.filter(user = request.user.ajeg_user, payment=False)

    for cart in carts:
        cart.payment = True
        cart.date = datetime.datetime.now()
        cart.save()

        print(carts)

    context = {
        "carts": carts,
        "date": datetime.datetime.now(),
        "user": request.user


@csrf_exempt
def get_cart_json(request):
    cart = Cart.objects.filter(user=request.user.ajeg_user)
    return HttpResponse(
        serializers.serialize("json", cart), content_type="application/json"
    )


@csrf_exempt
def get_product_json(request):
    product_id = request.GET.get("product_id")
    product = Product.objects.get(pk=product_id)
    return HttpResponse(
        serializers.serialize("json", [product]), content_type="application/json"
    )


@csrf_exempt
def update_cart_quantity(request):
    data = json.loads(request.body)
    product_id = data["product_id"]
    quantity = data["quantity"]
    product = Product.objects.get(pk=product_id)

    cart = Cart.objects.get(product=product_id, user=request.user.ajeg_user)
    cart.quantity = quantity
    cart.total_price = product.price * quantity
    print("total price", cart.total_price)
    cart.save()

    return JsonResponse(
        {
            "message": "Cart quantity updated succesfully",
            "total_price": cart.total_price,
        },
        safe=False,
    )


@csrf_exempt
def store_page(request, pk):
    store = Store.objects.get(pk=pk)
    products = Product.objects.filter(store=store)

    user = None
    if request.user.is_authenticated:
        user = request.user.ajeg_user

    context= {
        'store': store,
        'products': products,
        'user': user,
        }
    return render(request, 'store_page.html', context)


@csrf_exempt
def delete_cart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    # product_id = request.GET.get('product_id')
    cart = Cart.objects.get(product_id=product_id, user=request.user.ajeg_user)
    print(cart)
    try:
        cart.delete()
    except Exception as e:
        print(e)
    # return render(request, 'checkout:show_cart')
    # print("cart", cart.product_id)
    return JsonResponse({'message': 'Cart item deleted'}, safe=False)
