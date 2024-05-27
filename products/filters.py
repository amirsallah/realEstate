import django_filters

from products.models import Estate


class EstateFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_area = django_filters.NumberFilter(field_name='meterage', lookup_expr='gte')
    max_area = django_filters.NumberFilter(field_name='meterage', lookup_expr='lte')

    class Meta:
        model = Estate
        fields = ['min_price', 'max_price', 'min_area', 'max_area']
