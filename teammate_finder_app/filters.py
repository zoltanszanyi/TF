import django_filters
from .models import *

class Filter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ('gender', 'language', 'region', 'country', 'rank', 'role1','role2','role3','role4','role5') 