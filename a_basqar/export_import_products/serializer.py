from rest_framework import serializers

from .models import (
    ImShoppingCartObject,
    ImportProduct,
    ExShoppingCartObject,
    ExportProduct
)
from products.serializer import (
    EachStoreProductProductSerializer
)
from company_management.serializers import (
    ContragentSerializer
)
from account.models import (
    Account
)
from products.models import (
    StoreProduct
)


class ImShoppingCartObjSerializer(serializers.ModelSerializer):
    import_contragent = ContragentSerializer(read_only=True)

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
        # fields = ('import_product', 'im_shopping_car_obj', 'prod_amount_in_cart')
        fields = ('import_product', 'prod_amount_in_cart')



class EditProductCountInImportCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportProduct
        fields = ('im_prod_id', 'prod_amount_in_cart')


class MakeImportSerializer(serializers.ModelSerializer):
    import_contragent = ContragentSerializer(read_only=True)
    class Meta:
        model = ImShoppingCartObject
        fields = ('cash_sum', 'import_contragent')


class ExShoppingCartObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExShoppingCartObject
        fields = "__all__"


class ExportProductsSerializer(serializers.ModelSerializer):
    export_product = EachStoreProductProductSerializer(read_only=True)

    class Meta:
        model = ExportProduct
        fields = "__all__"


class CreateNewExportCartObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExShoppingCartObject
        fields = ()


class AddProdToExShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExportProduct
        fields = ('export_product', 'ex_shopping_car_obj', 'prod_amount_in_cart')


class EditProductCountInExportCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExportProduct
        fields = ('ex_prod_id', 'prod_amount_in_cart')
