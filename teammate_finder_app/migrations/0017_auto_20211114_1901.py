# Generated by Django 3.2.8 on 2021-11-14 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teammate_finder_app', '0016_auto_20211114_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]