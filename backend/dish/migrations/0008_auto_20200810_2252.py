# Generated by Django 3.1 on 2020-08-10 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0007_remove_dish_water'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='carbohydrate',
            new_name='carbohydrates',
        ),
    ]