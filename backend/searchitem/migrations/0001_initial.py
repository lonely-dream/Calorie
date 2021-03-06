# Generated by Django 3.0.2 on 2020-01-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='search item')),
                ('search_time', models.IntegerField(verbose_name='search_time')),
            ],
            options={
                'verbose_name': 'SearchItem',
                'verbose_name_plural': 'SearchItems',
            },
        ),
    ]
