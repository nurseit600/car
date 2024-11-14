# Generated by Django 5.1.3 on 2024-11-12 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=16, unique=True, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('have', models.BooleanField(default=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
