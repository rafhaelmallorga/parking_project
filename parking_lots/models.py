from django.db import models


class ParkingLot(models.Model):
    name = models.CharField(max_length=127)
    is_active = models.BooleanField(default=True)

    owner = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="parking_lots",
    )
