from urllib.parse import urlparse

from django.urls import path

from . import views

urlpatterns = [
    path("parking-lots/", views.ListCreateParkingLotView.as_view()),
    path(
        "parking-lots/<int:parking_lot_id>/",
        views.RetrieveUpdateDestroyParkingLotView.as_view(),
    ),
]
