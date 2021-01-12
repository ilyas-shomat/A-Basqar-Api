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

######################################################################################
# --------------- MOVEMENT -------------------------------------------------------------
######################################################################################


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



######################################################################################
# --------------- ORDERING -------------------------------------------------------------
######################################################################################

class OrderingObjectSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrderingObject
        fields = "__all__"


class OrderingProductsSerializer(serializers.ModelSerializer):
    ordering_product = EachStoreProductProductSerializer(read_only=True)
    class Meta: 
        model = OrderingProduct
        fields = "__all__"


class CreateNewOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderingObject
        fields = ()


class AddProdToOrderingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderingProduct
        fields = ('ordering_product','product_amount')


class EditProductCountInOrderingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderingProduct
        fields = ('ordering_prod_id', 'product_amount')

