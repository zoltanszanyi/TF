# Generated by Django 3.2.8 on 2021-11-05 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammate_finder_app', '0010_auto_20211105_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roles',
        ),
        migrations.AddField(
            model_name='profile',
            name='text',
            field=models.TextField(default='anonymous', verbose_name='Roles'),
            preserve_default=False,
        ),
    ]