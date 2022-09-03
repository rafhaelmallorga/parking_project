from accounts.serializers import OwnerSerializer
from rest_framework import serializers

from .models import ParkingLot


class CreateParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = "__all__"
        read_only_fields = ["owner"]


class ListParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = "__all__"

    owner = OwnerSerializer(read_only=True)
