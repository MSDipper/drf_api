from rest_framework import serializers
from hotel.models import Hotel, Reviews


class HotelSerializer(serializers.ModelSerializer):
    ''' Отели '''
    class Meta:
        model = Hotel
        fields = ('title', 'category')


class ReviewCreateSerializer(serializers.ModelSerializer):
    """ Добавление отзыва """
    class Meta:
        model = Reviews
        fields = '__all__'
        

class ReviewSerializer(serializers.ModelSerializer):
    """ Вывод отзыва """
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'message', 'parent')
        

class HotelDetailSerializer(serializers.ModelSerializer):
    ''' Апартаменты отеля '''
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewSerializer(many=True)
    
    
    class Meta:
        model = Hotel
        exclude = ('published',)