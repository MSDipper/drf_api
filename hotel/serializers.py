from rest_framework import serializers
from hotel.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    ''' Отели '''
    class Meta:
        model = Hotel
        fields = ('title', 'category')


class HotelDetailSerializer(serializers.ModelSerializer):
    ''' Апартаменты отеля '''
    class Meta:
        model = Hotel
        exclude = ('published',)