from rest_framework import serializers

from .models import (
    ImShoppingCartObject,
    ImportProducts
)

from products.serializer import (
    EachStoreProductProductSerializer
)

class ImShoppingCartObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImShoppingCartObject
        fields = "__all__"


class ImportProductsSerializer(serializers.ModelSerializer):
    import_product = EachStoreProductProductSerializer(read_only=True)

    class Meta:
        model = ImportProducts
        fields = ('im_prod_id', 'import_product')