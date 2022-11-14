from rest_framework.response import Response
from rest_framework.views import APIView
from hotel.models import Hotel
from hotel.serializers import HotelSerializer, HotelDetailSerializer


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