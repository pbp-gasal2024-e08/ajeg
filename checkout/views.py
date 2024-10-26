from itertools import product
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
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
        if Cart.objects.filter(user = user, product = product).exists():
            cart = Cart.objects.get(user = user, product = product)
            cart.quantity += form.cleaned_data['quantity']
            cart.total_price += product.price * form.cleaned_data['quantity']
            cart.save()
        else:
            cart = Cart.objects.create(
                user = user,
                product = product,
                quantity = form.cleaned_data['quantity'],
                total_price = product.price * form.cleaned_data['quantity']
            )

    context = {
        'product': product,
        'store': store,
        'form': form,
    }
    return render(request, 'product_page.html', context)

@csrf_exempt
@login_required
def show_cart(request):
    cart = Cart.objects.filter(user = request.user.ajeg_user)

    context = {
        'carts': cart
    }
    return render(request, 'cart_copy.html', context)

@login_required
def show_checkout(request):
    return render(request, 'checkout.html')

@login_required
def show_order_summary(request):
    return render(request, 'order_summary.html')

@login_required
def show_order_confirmation(request):
    return render(request, 'order_confirmation.html')

@csrf_exempt
def get_cart_json(request):
    cart = Cart.objects.filter(user = request.user.ajeg_user)
    return HttpResponse(serializers.serialize('json', cart), content_type='application/json')

@csrf_exempt
def get_product_json(request):
    product_id = request.GET.get('product_id')
    product = Product.objects.get(pk=product_id)
    return HttpResponse(serializers.serialize('json', [product]), content_type='application/json')
    
@csrf_exempt
def update_cart_quantity(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    print(product_id)
    quantity = data['quantity']
    print(quantity)
    product = Product.objects.get(pk=product_id)
    print(product)

    cart = Cart.objects.get(product=product_id, user=request.user.ajeg_user)
    print(cart)
    cart.quantity = quantity
    print(quantity)
    cart.total_price = product.price * quantity
    print(cart.total_price)
    cart.save()

    return JsonResponse({'message': 'Cart quantity updated succesfully'})