from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.context_processors import auth 

from main.models import Product
# Create your views here.


@login_required
def show_cart(request):
    return render(request, 'cart.html')


@login_required
def show_checkout(request):
    return render(request, 'checkout.html')

@login_required
def show_order_summary(request):
    return render(request, 'order_summary.html')

def show_product_page(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product.html', {'product': product})