# Generated by Django 5.1.7 on 2025-03-16 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0002_produit_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
