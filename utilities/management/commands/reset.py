import os, random, glob
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.db import connection, close_old_connections
from django.apps import apps
from myauth.models import AjegUser
from main.models import Product, Store
from favorites.models import FavoriteProductList, FavoriteStoreList, FavoriteProduct, FavoriteStore
from wishlist.models import Wishlist, WishlistItem

# To use        : py manage.py reset
# Used for      : insta-creating users with pre-hashed passwords, clean up migration history (Warning, will delete data from current database)
# Reccomended   : have fixtures and load them or extend this command to quickly reset/reload data

class Command(BaseCommand):
    help = 'Flush DB, delete sqlite file, apply migrations, load initial data, and create superuser/users.'
    connection.close()
    close_old_connections()

    def handle(self, *args, **kwargs):
        confirm = input("Warning, will flush current database (y/N) : ")
        if confirm == "y":
            call_command('flush', '--no-input')
            app_names = [app.label for app in apps.get_app_configs()]
            for app in app_names:
                migration_path = os.path.join(app, 'migrations', '*.py')
                for migration_file in glob.glob(migration_path):
                    if not migration_file.endswith('__init__.py'):
                        os.remove(migration_file)
                        print(f'Removed: {migration_file}')
            call_command('makemigrations')
            call_command('migrate')
            call_command('loaddata', 'data.json')
            User = get_user_model()
            User.objects.create_superuser('admin', 'admin@example.com', 'blank')
            self.stdout.write(self.style.SUCCESS('Superuser created: admin (password is "blank").'))
            users = [
                {"username": "traveller1", "email": "traveller1@example.com", "password": "password", "user_type": "traveller"},
                {"username": "merchant1", "email": "merchant1@example.com", "password": "password", "user_type": "merchant"},
            ]

            first_user = None

            for user_data in users:
                user = User(
                    username=user_data["username"],
                    email=user_data["email"],
                    is_staff=False,  
                    is_active=True,  
                )
                user.set_password(user_data["password"])  # Hash the password
                user.save()
                ajeg_user = AjegUser.objects.create(
                    ajeg_user=user,
                    user_type=user_data["user_type"]
                )
                if not first_user:
                    first_user = user
                self.stdout.write(self.style.SUCCESS(f'[{ajeg_user.user_type}] User {user.username} created. with password {user_data["password"]}'))

            # For favorites and wishlist
            store_ids = [1, 2]  
            product_ids = [1, 2]  

            favorite_store_list = FavoriteStoreList.objects.create(user=first_user)
            for store_id in store_ids:  
                favorite_store = FavoriteStore(favorite_list=favorite_store_list, store_id=store_id)
                favorite_store.save()

            favorite_product_list = FavoriteProductList.objects.create(user=first_user)
            for product_id in product_ids:  
                favorite_store = FavoriteProduct(favorite_list=favorite_product_list, product_id=product_id)
                favorite_store.save()

            wishlist = Wishlist.objects.create(user=first_user)
            for product_id in product_ids[:2]:  # Assuming you want the first two products in the wishlist
                wishlist_item = WishlistItem.objects.create(
                    wishlist=wishlist,
                    product_id=product_id,
                    amount=random.randint(1, 10)  # Set to any number, change as needed
                )
            #wishlist_item.save()
            #wishlist.save()
            #favorite_product_list.save()
            #favorite_store_list.save()
