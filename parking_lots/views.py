from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import ParkingLot
from .serializers import CreateParkingLotSerializer, ListParkingLotSerializer


class ListCreateParkingLotView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ParkingLot.objects.all()
    # serializer_class = CreateParkingLotSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateParkingLotSerializer

        return ListParkingLotSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()

        return self.queryset.filter(owner=self.request.user)
        # return self.request.user.parking_lots

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
