# Generated by Django 4.1.13 on 2024-02-21 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurantid', models.AutoField(primary_key=True, serialize=False)),
                ('restaurantname', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]
