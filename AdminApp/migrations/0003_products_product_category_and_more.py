# Generated by Django 5.0.4 on 2024-07-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_category',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_desc',
            field=models.TextField(default='null'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default='null', upload_to=''),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
    ]
