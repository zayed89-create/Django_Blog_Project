# Generated by Django 5.1.2 on 2024-11-23 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Female',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('female_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Male',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male_name', models.CharField(max_length=50, null=True)),
                ('girls', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.female')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
