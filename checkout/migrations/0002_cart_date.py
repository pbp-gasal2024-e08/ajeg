# Generated by Django 4.2.16 on 2024-10-27 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]