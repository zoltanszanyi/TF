from typing import Text
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.shortcuts import redirect
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/pic_2z37G75.png', upload_to='profile_pics')
    country = CountryField()
    gender = models.CharField(
        max_length = 6,
        choices=[('Male','Male'),('Female','Female')]
    )

    region = models.CharField(
        max_length = 21,
        choices = [('All regions', 'All regions'),
                   ('Brazil','Brazil'),
                   ('Europe Nordic & East', 'Europe Nordic & East'),
                   ('Europe West', 'Europe West'),
                   ('North America', 'North America'),
                   ('Latin America North','Latin America North'),
                   ('Latin America South', 'Latin America South'),
                   ('Oceania', 'Oceania'),
                   ('Russia', 'Russia'),
                   ('Turkey', 'Turkey')]
    )

    language = models.CharField(
        max_length = 37,
        choices = [('Czech', 'Czech'),
                   ('Greek','Greek'),
                   ('Polish', 'Polish'),
                   ('Romanian', 'Romanian'),
                   ('Hungarian', 'Hungarian'),
                   ('English (United Kingdom)','English (United Kingdom)'),
                   ('German', 'German'),
                   ('Spanish (Spain)', 'Spanish (Spain)'),
                   ('Spanish (Argentina)', 'Spanish (Argentina)'),
                   ('Portuguese (Brazil', 'Portuguese (Brazil)'),
                   ('English (United States)', 'English (United States)'),
                   ('English (Australia)', 'English (Australia)'),
                   ('Russian', 'Russian'),
                   ('Turkish', 'Turkish'),
                   ('Malay', 'Malay'),
                   ('English (Republic of the Philippines)', 'English (Republic of the Philippines)'),
                   ('English (Singapore)', 'English (Singapore)'),
                   ('Thai', 'Thai'),
                   ('Vietnamese', 'Vietnamese'),
                   ('Indonesian', 'Indonesian'),
                   ('Chinese (Malaysia)', 'Chinese (Malaysia)'),
                   ('Chinese (China)', 'Chinese (China)'),
                   ('Chinese (Taiwan)', 'Chinese (Taiwan)')]
    )
    rank = models.CharField(
        max_length = 11,
        choices = [('Iron', 'Iron'),
                   ('Bronze','Bronze'),
                   ('Silver', 'Silver'),
                   ('Gold', 'Gold'),
                   ('Platinum', 'Platinum'),
                   ('Diamond','Diamond'),
                   ('Master ', 'Master'),
                   ('Grandmaster', 'Grandmaster'),
                   ('Challenger', 'Challenger')]
    )

    role1 = models.BooleanField(default = False, verbose_name='TOP')
    role2 = models.BooleanField(default = False, verbose_name='JUNGLE')
    role3 = models.BooleanField(default = False, verbose_name='MID')
    role4 = models.BooleanField(default = False, verbose_name='ADC')
    role5 = models.BooleanField(default = False, verbose_name='SUPPORT')

    write = models.TextField('Write something about yourself')



    def __str__(self):
        return f'{self.user.username}'



# Create your models here.
