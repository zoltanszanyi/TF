# Generated by Django 3.2.8 on 2021-11-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammate_finder_app', '0009_profile_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role1',
            field=models.BooleanField(default=False, verbose_name='TOP'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role2',
            field=models.BooleanField(default=False, verbose_name='JUNGLE'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role3',
            field=models.BooleanField(default=False, verbose_name='MID'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role4',
            field=models.BooleanField(default=False, verbose_name='ADC'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role5',
            field=models.BooleanField(default=False, verbose_name='SUPPORT'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='roles',
            field=models.CharField(max_length=10),
        ),
    ]