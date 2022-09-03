from rest_framework import generics

from .models import ParkingLot
from .serializers import ParkingLotSerializer


class ListCreateParkingLotView(generics.ListCreateAPIView):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer
