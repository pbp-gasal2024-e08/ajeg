# Generated by Django 4.2.16 on 2024-10-15 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myauth', '0004_ajeguser__toko_delete_ajegmerchant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajeguser',
            name='ajeg_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ajeg_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
