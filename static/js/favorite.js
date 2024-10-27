document.addEventListener("DOMContentLoaded", function() {
    fetch("/favorites/get-favorite-ids")  
    .then(response => response.json())
    .then(data => {
        let favoritedIds = data.ids;  
        $('.toggle-favorite-button').each(function () {
            const button = $(this);
            const productId = button.data('product-id'); 
            const svg = button.find('svg');

            if (favoritedIds.includes(productId)) {
                svg.attr('fill', 'red');
            } else {
                svg.attr('fill', 'none');
            }
        });
        $('.toggle-favorite-button').on('click', function() {
            const button = $(this);
            const productId = button.data('product-id'); 
            const svg = button.find('svg');       
            const csrfToken = button.data('csrf');
            $.ajax({
                type: 'POST',
                url: '/favorites/toggle-product', 
                data: {
                    'product_id': productId,
                    'csrfmiddlewaretoken': csrfToken
                }
            }).then(function(response){
                if (response.is_favorited){
                    svg.attr('fill', 'red');
                }
                else{
                    svg.attr('fill', 'none');
                };
            }).catch(function(error) {
                console.error('Error toggling favorite:', error);
            });
        });
    }).catch(error => console.error('Error fetching favorite IDs:', error));
});

// For the button --> {% include 'favorite_button.html' with id=product.id csrf_token=csrf_token %}
// For referencing this <script src="{% static 'js/favorite.js' %}"></script>
// Requires <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>