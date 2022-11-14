from django.urls import path
from hotel.views import HotelListView


urlpatterns = [

    path('hotel/', HotelListView.as_view())
]
