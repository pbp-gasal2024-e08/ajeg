document.addEventListener("DOMContentLoaded", function() {
    fetch("/favorites/get-favorite-store-ids")  
    .then(response => response.json())
    .then(data => {
        let favoritedIds = data.ids;  
        $('.toggle-favorite-store').each(function () {
            const button = $(this);
            const storeId = button.data('store-id'); 
            const svg = button.find('svg');

            if (favoritedIds.includes(storeId)) {
                svg.attr('fill', 'red');
            } else {
                svg.attr('fill', 'none');
            }
        });
        $('.toggle-favorite-store').on('click', function() {
            const button = $(this);
            const storeId = button.data('store-id'); 
            const svg = button.find('svg');       
            const csrfToken = button.data('csrf');
            $.ajax({
                type: 'POST',
                url: '/favorites/toggle-store', 
                data: {
                    'store_id': storeId,
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

// For the button --> {% include 'favorite_store.html' with id=store.id csrf_token=csrf_token %}
// For referencing this <script src="{% static 'js/favorite_store.js' %}"></script>
// Requires <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>