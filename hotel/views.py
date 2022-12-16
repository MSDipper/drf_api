from rest_framework.response import Response
from rest_framework.views import APIView
from hotel.models import Hotel
from hotel.serializers import (
                            HotelSerializer,
                            HotelDetailSerializer,
                            ReviewCreateSerializer,
                            CreateRatingSerializer
                            )


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


class AddStarRatingView(APIView):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=self.get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)