# Generated by Django 5.1.2 on 2024-11-23 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_test_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
