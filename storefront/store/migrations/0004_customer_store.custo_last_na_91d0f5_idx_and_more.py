# Generated by Django 4.0.1 on 2022-01-31 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_products_slug'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store.custo_last_na_91d0f5_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store.customers',
        ),
    ]
