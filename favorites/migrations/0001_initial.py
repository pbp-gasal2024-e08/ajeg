<<<<<<< HEAD
# Generated by Django 5.1.2 on 2024-10-27 16:00
=======
# Generated by Django 5.1.1 on 2024-10-27 15:50
>>>>>>> b47bcb5a4a957bf187cf67c6bc81198ef39410f2

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_product_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('favorite_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='favorites.favoriteproductlist')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteStoreList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_store_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.store')),
                ('favorite_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='favorites.favoritestorelist')),
            ],
        ),
    ]
