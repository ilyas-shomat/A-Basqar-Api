from rest_framework import serializers

from .models import (
    MovementObject,
    MovementProduct,
    OrderingObject,
    OrderingProduct
)

from account.models import (
    Account,
    Store
)

from products.serializer import (
    EachStoreProductProductSerializer
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

class MovementProductsSerializer(serializers.ModelSerializer):
    movement_product = EachStoreProductProductSerializer(read_only=True)
    class Meta: 
        model = MovementProduct
        fields = "__all__"


class AddProdToMovementCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovementProduct
        fields = ('movement_product','product_amount')

class EditProductCountInMovementCartSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MovementProduct
        fields = ('movement_prod_id', 'product_amount')


class MakeMovementHistorySerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    class Meta:
        model = MovementObject
        fields = ('store', )

class OrderingObjectSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrderingObject
        fields = "__all__"

