from rest_framework import permissions
from rest_framework.views import Request, View

from .models import ParkingLot


class IsParkingLotOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, parking_lot: ParkingLot
    ) -> bool:
        return parking_lot.owner == request.user or request.user.is_superuser
