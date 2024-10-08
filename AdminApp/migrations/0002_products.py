# Generated by Django 5.0.4 on 2024-07-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_price', models.IntegerField()),
                ('product_desc', models.TextField()),
                ('product_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
