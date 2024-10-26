from django.shortcuts import render
from wishlist.models import Wishlist, WishlistItem
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def add_to_wishlist(request, product_id):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item = WishlistItem.objects.filter(wishlist=wishlist, product_id=product_id)
    
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
    wishlistitem = WishlistItem.objects.filter(wishlist=wishlist, product_id=product_id)

    if wishlistitem:
        wishlistitem.delete()
        messages.info(request, "Item removed from wishlist.")
        return JsonResponse({"deleted": True})
    else:
        return JsonResponse({"deleted": False})

def edit_wishlist(request, product_id):
    if request.method == "POST":
        new_amount = int(request.POST.get("amount", 1))
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist_item = WishlistItem.objects.filter(wishlist=wishlist, product_id=product_id)
        if new_amount > 0:
            wishlist_item.amount = new_amount
            wishlist_item.save()
            return JsonResponse({"deleted": False, "amount": wishlist_item.amount})
        else:
            wishlist_item.delete()
            return JsonResponse({"deleted": True})



def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist.items.all()
    return render(request, 'wishlist.html', context={
        'wishlist': wishlist, 
    })

AJAX = """
function adjustWishlistQuantity(productId, action) {
    const quantityElement = $(`#wishlist-item-quantity-${productId}`);
    let currentQuantity = parseInt(quantityElement.text());

    let newQuantity = action === 'increment' ? currentQuantity + 1 : currentQuantity - 1;
    if (newQuantity < 1) {
        newQuantity = 1;  // Set a minimum quantity of 1
    }

    $.ajax({
        url: `/wishlist/edit/${productId}/`,
        type: 'POST',
        data: {
            'quantity': newQuantity,
            'csrfmiddlewaretoken': '{{ csrf_token }}',  // Ensure CSRF token for security
        },
        success: function(response) {
            if (response.deleted === false) {
                quantityElement.text(response.quantity);  // Update quantity on the page
            } else if (response.sdeleted === true) {
                $(`#wishlist-item-${productId}`).remove();  // Remove item if quantity set to 0
            }
        },
        error: function() {
            alert("There was an error updating the wishlist.");
        }
    });
}
"""

button = """
<div id="wishlist-item-{{ product.id }}">
    <button onclick="adjustWishlistQuantity({{ product.id }}, 'decrement')">-</button>
    <span id="wishlist-item-quantity-{{ product.id }}">{{ wishlist_item.quantity }}</span>
    <button onclick="adjustWishlistQuantity({{ product.id }}, 'increment')">+</button>
</div>
"""