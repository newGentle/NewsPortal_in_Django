# Generated by Django 4.1.7 on 2023-03-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]