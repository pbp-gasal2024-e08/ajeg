from django.shortcuts import render
from favorites.models import FavoriteProductList, FavoriteStoreList, FavoriteStore, FavoriteProduct
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def favorite_store(request):
    store_id = request.POST.get('store_id')
    favorite_list, created = FavoriteStoreList.objects.get_or_create(user=request.user)
    favorite_item = FavoriteStore.objects.filter(favorite_list=favorite_list, store_id=store_id)
    
    if favorite_item:
        favorite_item.delete()
        messages.info(request, "Store unfavorited.")
        is_favorited = False
    else:
        # Step 3: Add the product to the favorites
        FavoriteStore.objects.create(favorite_list=favorite_list, store_id=store_id)
        messages.success(request, "Store favorited.")
        is_favorited = True
    
    return JsonResponse({'is_favorited': is_favorited})


def favorite_product(request): 
    product_id = request.POST.get('product_id')
    favorite_list, created = FavoriteProductList.objects.get_or_create(user=request.user)
    favorite_item = FavoriteProduct.objects.filter(favorite_list=favorite_list, product_id=product_id)
    
    if favorite_item:
        favorite_item.delete()
        messages.info(request, "Product unfavorited.")
        is_favorited = False
    else:
        FavoriteProduct.objects.create(favorite_list=favorite_list, product_id=product_id)
        messages.success(request, "Product favorited.")
        is_favorited = True
    
    return JsonResponse({'is_favorited': is_favorited})


def view_favorites(request):
    favorite_product_list, created = FavoriteProductList.objects.get_or_create(user=request.user)
    favorite_store_list, created = FavoriteStoreList.objects.get_or_create(user=request.user)
    favorite_stores = favorite_store_list.items.all()
    favorite_products  = favorite_product_list.items.all()
    return render(request, 'favorites.html', context={
        'favorite_stores': favorite_stores, 
        'favorite_products' : favorite_products
    })

script_store = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    const favoriteButtons = document.querySelectorAll(".favorite-toggle-store");

    favoriteButtons.forEach(button => {
        button.addEventListener("click", function() {
            const storeId = this.dataset.storeId;
            const csrfToken = "{{ csrf_token }}";  
            
            const url = `{% url 'favorites/toggle_store' 0 %}`.replace("0", storeId);

            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.is_favorited) {
                    this.classList.add("favorited");  // Add filled heart style
                } else {
                    this.classList.remove("favorited");  // Remove filled heart style
                }
            });
        });
    });
});
</script>
"""

button_store = """
<button class="favorite-toggle-store {% if product in user.favorite_store_list.items.all %}favorited{% endif %}" data-store-id="{{ store.id }}">
    <i class="heart-icon"></i>  
</button>
"""
