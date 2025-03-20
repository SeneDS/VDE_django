# Generated by Django 5.1.7 on 2025-03-19 10:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0006_alter_produit_date_alter_produit_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
