# Generated by Django 4.1.2 on 2022-11-03 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_category_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subscription',
            new_name='subscribers',
        ),
    ]