from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from hotel.models import Hotel
from hotel.serializers import HotelSerializer


class HotelApiTestCase(APITestCase):
    def test_get(self):
        hotel_1 = Hotel.objects\
            .create(title='Paris', slug='paris', price=123, quantity=12, gps='russia',description='lorem ipsum', name_video='lorem')
        hotel_2 = Hotel.objects\
            .create(title='Italy', slug='italy', price=323, quantity=12, gps='russia',description='lorem ipsum', name_video='lorem')
        url = reverse('hotel')
        print(url)
        response = self.client.get(url)
        serializer_data = HotelSerializer([hotel_1, hotel_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)