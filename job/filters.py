import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['published_at' , 'salary' , 'image' , 'vacancy' , 'owner' , 'slug']