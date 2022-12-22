from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from hotel.models import Hotel
from rest_framework.permissions import IsAuthenticated
from hotel.service import get_client_ip, HotelFilter
from django.db import models
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from hotel.serializers import (
                            HotelSerializer,
                            HotelDetailSerializer,
                            ReviewCreateSerializer,
                            CreateRatingSerializer
                            )


class HotelListView(generics.ListAPIView):
    ''' Вывод отелей '''
    serializer_class = HotelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = HotelFilter
    permission_classes = [IsAuthenticated]
    search_fields = ['title', 'gps']
    ordering_fields = ['quantity', 'rating', 'price',]
    
    
    def get_queryset(self):
        hotels = Hotel.objects.filter(published=True).annotate(
            rating=models.Count("ratings", 
                                filter=models.Q(ratings__ip=get_client_ip(self.request))
                                )
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return hotels


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
    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)


def auth(request):
    return render(request, 'oauth.html')