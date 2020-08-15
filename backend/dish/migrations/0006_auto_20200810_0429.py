# Generated by Django 3.1 on 2020-08-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0005_auto_20200131_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='calcium',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='calcium'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='dietary_fiber',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='dietary fiber'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='vitaminC',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Vitamin C'),
            preserve_default=False,
        ),
    ]
