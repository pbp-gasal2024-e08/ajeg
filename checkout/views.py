from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from checkout.forms import AddToCartForm
from checkout.models import Cart
from main.models import Product, Store
from myauth.models import AjegUser

# Create your views here.
def show_product_page(request, pk):
    product = Product.objects.get(pk=pk)
    store = Store.objects.get(pk=product.store_id)
    user = AjegUser.objects.get(ajeg_user=request.user)

    form = AddToCartForm(request.POST)
    print(form.data)
    print(form.is_valid())
    if form.is_valid():
        if Cart.objects.filter(user = user, product = product).exists():
            print('exists')
            cart = Cart.objects.get(user = user, product = product)
            print(cart)
            print(cart.quantity, 'before')
            cart.quantity += form.cleaned_data['quantity']
            print(cart.quantity, 'after')
            print(cart.total_price, 'before')
            cart.total_price += product.price * form.cleaned_data['quantity']
            cart.save()
        else:
            print('not exists')
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


@login_required
def show_cart(request):
    cart = Cart.objects.filter(user = request.user.ajeg_user)

    context = {
        'carts': cart
    }
    return render(request, 'cart.html', context)


@login_required
def show_checkout(request):
    return render(request, 'checkout.html')

@login_required
def show_order_summary(request):
    return render(request, 'order_summary.html')

@login_required
def show_order_confirmation(request):
    return render(request, 'order_confirmation.html')


