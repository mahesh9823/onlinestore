# Generated by Django 4.2.4 on 2023-08-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerModel',
            fields=[
                ('sellerId', models.IntegerField(primary_key=True, serialize=False)),
                ('sellerName', models.CharField(max_length=50)),
                ('sellerDetails', models.TextField(null=True)),
                ('sellerEmailId', models.CharField(max_length=100, unique=True)),
                ('sellerPassword', models.CharField(max_length=12)),
                ('sellerContactNo', models.CharField(max_length=12)),
            ],
        ),
    ]