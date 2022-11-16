from rest_framework.response import Response
from rest_framework.views import APIView
from hotel.models import Hotel
from hotel.serializers import HotelSerializer, HotelDetailSerializer, ReviewCreateSerializer
from rest_framework import serializers


class HotelListView(APIView):
    ''' Вывод отелей '''
    def get(self, request):
        hotels = Hotel.objects.filter(published=True)
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)


class HotelDetailView(APIView):
    ''' Вывод апартаментов отеля''' 
    def get(self, request, pk):
        hotel = Hotel.objects.filter(id=pk, published=True)
        serializer = HotelDetailSerializer(hotel, many=True)
        return Response(serializer.data)





class ReviewCreateView(APIView):
    """ Добавление отзыва к фильму """
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)

