import django_filters
from django.db.models import Q
from .models import Blog

class BlogFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='filter_by_all_text', label='Search')
    author__username = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains', label='Author')

    class Meta:
        model = Blog
        fields = ['q', 'author__username']

    def filter_by_all_text(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(title__icontains=value) | Q(body__icontains=value)
            )
        return queryset