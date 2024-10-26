# Generated by Django 5.1.1 on 2024-10-24 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreview',
            name='base_comment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.comment'),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
