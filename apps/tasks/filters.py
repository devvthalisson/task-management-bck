import django_filters
from .models import Task
from django.utils import timezone


class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter()
    recents = django_filters.BooleanFilter(label='recents', method='filter_recents')

    class Meta:
        model = Task
        fields = {
            'title': ['iexact', 'icontains'],
        }

    def filter_recents(self, queryset, name, value):
        today = timezone.now().date()
        if value:
            return queryset.filter(created_at__date__gte=today)
        return queryset