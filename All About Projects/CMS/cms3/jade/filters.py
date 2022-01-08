import django_filters
from django_filters import DateFilter
from .models import *


class CommentFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="created", lookup_expr="gte")
    # enddate = DateFilter(field_name="created", lookup_expr="lte")
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['created','Name']
