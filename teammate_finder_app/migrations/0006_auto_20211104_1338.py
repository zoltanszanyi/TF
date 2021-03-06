# Generated by Django 3.2.8 on 2021-11-04 12:38

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teammate_finder_app', '0005_auto_20211104_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='language',
            field=django_countries.fields.CountryField(default='anonymous', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(choices=[('All regions', 'All regions'), ('Brazil', 'Brazil'), ('Europe Nordic & East', 'Europe Nordic & East'), ('Europe West', 'Europe West'), ('North America', 'North America'), ('Latin America North', 'Latin America North'), ('Latin America South', 'Latin America South'), ('Oceania', 'Oceania'), ('Russia', 'Russia'), ('Turkey', 'Turkey')], max_length=21),
        ),
    ]
