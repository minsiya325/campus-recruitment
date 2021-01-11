import django_filters
from django_filters import DateFilter

from .models import *

class AcademicFilter(django_filters.FilterSet):
    class Meta:
        model = Academic

        fields = ['sem','batch','course__name']

class PlaceFilter(django_filters.FilterSet):
    class Meta:
        model = PlacedStudent

        fields = ['place_status']

class CompnayFilter(django_filters.FilterSet):
    class Meta:
        model = Reg

        fields = ['user__first_name','joindate']