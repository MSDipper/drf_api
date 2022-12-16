from django.urls import path
from hotel.views import (
                        HotelListView,
                        HotelDetailView, 
                        ReviewCreateView,
                        AddStarRatingView
                        )


urlpatterns = [
    path('hotel/<int:pk>/', HotelDetailView.as_view()),
    path('hotel/', HotelListView.as_view(), name='hotel'),
    path('review/', ReviewCreateView.as_view()),
    path('rating/', AddStarRatingView.as_view()),
]
