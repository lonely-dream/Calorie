# Generated by Django 3.0.2 on 2020-01-30 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0002_auto_20200128_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='like',
        ),
    ]
