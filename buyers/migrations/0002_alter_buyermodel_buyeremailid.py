# Generated by Django 4.2.4 on 2023-08-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyermodel',
            name='buyerEmailId',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
