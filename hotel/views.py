from rest_framework.response import Response
from rest_framework.views import APIView
from hotel.models import Hotel
from hotel.serializers import HotelSerializer


class HotelListView(APIView):
    ''' Вывод отелей '''
    def get(self, request):
        hotels = Hotel.objects.filter(published=True)
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)
