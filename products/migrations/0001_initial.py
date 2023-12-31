# Generated by Django 4.2.4 on 2023-08-03 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_rename_category_categorymodel'),
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=50, unique=True)),
                ('productDetails', models.TextField()),
                ('productPrice', models.IntegerField(default=0)),
                ('productStock', models.IntegerField(default=0)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.categorymodel')),
                ('sellerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='sellers.sellermodel')),
            ],
        ),
    ]
