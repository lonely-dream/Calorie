# Generated by Django 3.0.2 on 2020-02-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchitem', '0002_historysearch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchitem',
            name='search_time',
        ),
        migrations.AddField(
            model_name='searchitem',
            name='category',
            field=models.CharField(choices=[('keyword', 'keyword'), ('tag', 'tag')], default='tag', max_length=10, verbose_name='search category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchitem',
            name='count',
            field=models.IntegerField(default=0, verbose_name='search count'),
            preserve_default=False,
        ),
    ]
