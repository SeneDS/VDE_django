# Generated by Django 5.1.7 on 2025-03-16 11:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_alter_produit_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='active',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='produit',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='produit',
            name='nom',
            field=models.CharField(blank=True, max_length=220),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10000),
        ),
    ]
