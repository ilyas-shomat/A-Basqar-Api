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