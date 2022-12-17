from django_filters import rest_framework as filters
from hotel.models import Hotel


def get_client_ip(request):
    """Получение IP пользоваеля"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class HotelFilter(filters.FilterSet):
    quantity = filters.RangeFilter()

    class Meta:
        model = Hotel
        fields = ['quantity']