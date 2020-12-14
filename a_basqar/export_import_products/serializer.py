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
        fields = ('im_prod_id', 'import_product')


class CreateNewImportCartObjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ()

class AddProdToImShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportProduct

#
# class AddProdToImShoppingCartSerializer(serializers.ModelSerializer):
#     product_id = serializers.IntegerField()
#     import_prod_count = serializers.IntegerField()
#     account_id = serializers.CharField(max_length=250)
#
#     # class Meta:
#     #     fields = ('product_id', 'import_prod_count', "account_id")
#
#     def save(self, **kwargs):
#         curr_cart_obj = ImShoppingCartObject.objects.get(status="current")
#         account = Account.objects.get(account_id=self.account_id)
#         store_product = StoreProduct.objects.get(product_id=self.product_id)
#         if curr_cart_obj is None:
#             new_current_object = ImShoppingCartObject()
#             new_current_object.status = "current"
#             new_current_object.account = account
#             new_current_object.save()
#
#             new_import_prod = ImportProduct()
#             new_import_prod.im_shopping_car_obj = new_current_object
#             new_import_prod.import_product = store_product
#             new_import_prod.save()

            # new_current_object.account =



        # current_cart_object = ImShoppingCartObject.objects.get(status="current")
        # if current_cart_object is None:
        #     new_current_object = ImShoppingCartObject()
        #     new_current_object.status = "current"
        #     new_current_object.account = user
        #
        #     new_import_objc_ser = ImportShoppingCartEmptySerializer(new_current_object, data=request.data)
        #
        #     if new_import_objc_ser.is_valid():
        #         new_import_objc_ser.save()
        #         store_product = StoreProduct.objects.get(product_id=store_product_id)
        #
        #         new_cart_product = ImportProduct()
        #         new_cart_product.im_shopping_car_obj = new_current_object
        #         new_cart_product.import_product = store_product


# class ImportShoppingCartEmptySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ImShoppingCartObject
#         fields = ()
#
# class AddProductToImportCart(serializers.ModelSerializer):
#
#     class Meta:
#         model = ImShoppingCartObject
#         fields = ()

