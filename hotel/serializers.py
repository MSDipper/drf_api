from rest_framework import serializers
from hotel.models import Hotel, Reviews


class HotelSerializer(serializers.ModelSerializer):
    ''' Отели '''
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Hotel
        fields = ('id', 'title', 'category')


class FiterReviewListSerializer(serializers.ListSerializer):
    """ Вывод зписи без дублирования """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """ Вывод рекурсивно children """ 
    def to_representation(self, value):
        serializers = self.parent.parent.__class__(value, context=self.context)
        return serializers.data

class ReviewCreateSerializer(serializers.ModelSerializer):
    """ Добавление отзыва """
    class Meta:
        model = Reviews
        fields = '__all__'
        

class ReviewSerializer(serializers.ModelSerializer):
    """ Вывод отзыва """
    children = RecursiveSerializer(many=True)
    
    class Meta:
        list_serializer_class = FiterReviewListSerializer
        model = Reviews
        fields = ('name', 'email', 'message', 'children')
        

class HotelDetailSerializer(serializers.ModelSerializer):
    ''' Апартаменты отеля '''
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewSerializer(many=True)
    
    
    class Meta:
        model = Hotel
        exclude = ('published',)