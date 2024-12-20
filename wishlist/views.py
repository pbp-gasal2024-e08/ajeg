from django.shortcuts import render
from wishlist.models import Wishlist, WishlistItem
from favorites.models import FavoriteProduct, FavoriteProductList
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.


def add_to_wishlist(request, product_id):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item = WishlistItem.objects.filter(
        wishlist=wishlist, product_id=product_id
    )

    if wishlist_item:
        wishlist_item.quantity += 1
        messages.info(request, "Added to wishlist.")
        wishlist_item.save()
    else:
        wishlist_item.quantity = 1
        messages.info(request, "Added to wishlist.")
        wishlist_item.save()

    return JsonResponse({"quantity": wishlist_item.amount})


def delete_from_wishlist(request, product_id):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlistitem = WishlistItem.objects.filter(
        wishlist=wishlist, product_id=product_id
    )

    if wishlistitem:
        wishlistitem.delete()
        messages.info(request, "Item removed from wishlist.")
        return JsonResponse({"deleted": True})
    else:
        return JsonResponse({"deleted": False})


def edit_wishlist(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        new_amount = int(request.POST.get("amount", 1))
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist_item = WishlistItem.objects.filter(
            wishlist=wishlist, product_id=product_id
        ).first()
        if new_amount > 0:
            total = int(
                float(request.POST.get("total"))
            ) + wishlist_item.product.price * (
                new_amount - wishlist_item.amount
            )
            total_formated = f"{int(total):,}".replace(",", ".")
            wishlist_item.amount = new_amount
            wishlist_item.save()
            new_total = f"{int(wishlist_item.amount * wishlist_item.product.price):,}".replace(
                ",", "."
            )
            return JsonResponse(
                {
                    "deleted": False,
                    "amount": wishlist_item.amount,
                    "item_total": new_total,
                    "total": total,
                    "total_formated": total_formated,
                }
            )
        else:
            wishlist_item.delete()
            return JsonResponse({"deleted": True})


def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist.items.all()
    favoriteproductlist, created = FavoriteProductList.objects.get_or_create(
        user=request.user
    )
    favorite_ids = favoriteproductlist.items.values_list(
        "product", flat=True
    ).distinct()
    total_price = int(
        sum(item.product.price * item.amount for item in wishlist)
    )
    return render(
        request,
        "wishlist.html",
        context={
            "wishlist": wishlist,
            "total": total_price,
            "favorited_ids": favorite_ids,
        },
    )
