# Generated by Django 3.0.2 on 2020-01-31 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200130_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=None, verbose_name='user avatar'),
        ),
    ]
