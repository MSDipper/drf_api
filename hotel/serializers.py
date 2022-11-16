from rest_framework import serializers
from hotel.models import Hotel, Reviews


class HotelSerializer(serializers.ModelSerializer):
    ''' Отели '''
    class Meta:
        model = Hotel
        fields = ('title', 'category')


class HotelDetailSerializer(serializers.ModelSerializer):
    ''' Апартаменты отеля '''
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    
    class Meta:
        model = Hotel
        exclude = ('published',)
        

class ReviewCreateSerializer(serializers.ModelSerializer):
    """ Добавление отзыва """
    class Meta:
        model = Reviews
        fields = '__all__'