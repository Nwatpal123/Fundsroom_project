# Generated by Django 4.1.13 on 2024-02-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
