# Generated by Django 5.1.2 on 2024-10-27 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField()),
                ("price_range", models.CharField(max_length=10)),
                ("rating", models.FloatField()),
                ("category", models.ManyToManyField(to="main.category")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="produk", max_length=255)),
                ("price", models.IntegerField()),
                ("description", models.TextField(default="Deskripsi Kosong")),
                ("imgurl", models.URLField(blank=True, null=True)),
                ("review_count", models.IntegerField(default=0, null=True)),
                (
                    "average_rating",
                    models.PositiveSmallIntegerField(default=0, null=True),
                ),
                (
                    "store",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="main.store",
                    ),
                ),
            ],
        ),
    ]
