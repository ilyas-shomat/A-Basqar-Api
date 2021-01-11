from rest_framework import serializers

from .models import (
    MovementObject,
    MovementProduct
)

from account.models import (
    Account,
    Store
)

from account.serializers import (
    StoreSerializer
)

class MovementObjectSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    class Meta:
        model = MovementObject
        fields = "__all__"

class CreateNewMovementObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovementObject
        fields = ()


class AddProdToMovementCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovementProduct
        fields = ('movement_product','product_amount')