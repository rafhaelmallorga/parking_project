from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .mixins import SerializerByMethodMixin
from .models import ParkingLot
from .permissions import IsParkingLotOwnerOrAdmin
from .serializers import DetailedParkingLotSerializer, ParkingLotSerializer


class ListCreateParkingLotView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ParkingLot.objects.all()
    # serializer_class = ParkingLotSerializer

    serializer_map = {
        "GET": DetailedParkingLotSerializer,
        "POST": ParkingLotSerializer,
    }

    # def get_serializer_class(self):
    #     # if self.request.method == "POST":
    #     #     return ParkingLotSerializer

    #     # return DetailedParkingLotSerializer

    #     return self.serializer_map.get(self.request.method)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()

        return self.queryset.filter(owner=self.request.user)
        # return self.request.user.parking_lots

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyParkingLotView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsParkingLotOwnerOrAdmin]

    queryset = ParkingLot.objects.all()
    # serializer_class = ParkingLotSerializer

    lookup_url_kwarg = "parking_lot_id"

    # def get_serializer_class(self):
    #     if self.request.method == "PATCH":
    #         return ParkingLotSerializer

    #     return DetailedParkingLotSerializer

    serializer_map = {
        "GET": DetailedParkingLotSerializer,
        "PATCH": ParkingLotSerializer,
    }
