# Generated by Django 4.2.3 on 2023-12-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_products_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='shirts'),
            preserve_default=False,
        ),
        
    ]