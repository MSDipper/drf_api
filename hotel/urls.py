from django.urls import path
from hotel.views import HotelListView, HotelDetailView


urlpatterns = [
    path('hotel/<int:pk>/', HotelDetailView.as_view()),
    path('hotel/', HotelListView.as_view())
]
