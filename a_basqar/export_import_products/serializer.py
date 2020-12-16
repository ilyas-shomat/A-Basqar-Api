from rest_framework import serializers

from .models import (
    ImShoppingCartObject,
    ImportProduct
)

from products.serializer import (
    EachStoreProductProductSerializer
)

from account.models import (
    Account
)

from products.models import (
    StoreProduct
)


class ImShoppingCartObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImShoppingCartObject
        fields = "__all__"


class ImportProductsSerializer(serializers.ModelSerializer):
    import_product = EachStoreProductProductSerializer(read_only=True)

    class Meta:
        model = ImportProduct
        fields = "__all__"


class CreateNewImportCartObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImShoppingCartObject
        fields = ()


class AddProdToImShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportProduct
        fields = ('import_product', 'im_shopping_car_obj', 'prod_amount_in_cart')


class EditProductCountInImportCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportProduct
        fields = ('im_prod_id', 'prod_amount_in_cart')
