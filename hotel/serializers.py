from rest_framework import serializers
from hotel.models import Hotel, Reviews, Rating


class HotelSerializer(serializers.ModelSerializer):
    ''' Отели '''
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    rating = serializers.BooleanField()
    middle_star = serializers.IntegerField()
    quantity = serializers.IntegerField()
    
    
    class Meta:
        model = Hotel
        fields = ('id', 'title', 'category', 'rating', 'middle_star', 'quantity',)


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


class CreateRatingSerializer(serializers.ModelSerializer):
    ''' Добавление рейтинга пользователем '''
    class Meta:
        model = Rating
        fields = ('star', 'hotel')
    
    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip = validated_data.get('ip', None),
            hotel = validated_data.get('hotel', None),
            defaults = {'star': validated_data.get('star')}
        )
        return rating