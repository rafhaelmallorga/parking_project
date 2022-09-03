from rest_framework import serializers

from .models import Account


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "is_active",
            "is_supperuser",
            "date_joined",
        ]

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
