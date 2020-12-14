from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    ImportProduct,
    ImShoppingCartObject
)
from .serializer import (
    ImportProductsSerializer,
    ImShoppingCartObjSerializer,
    # ImportShoppingCartEmptySerializer,
    # AddProductToImportCart,
    AddProdToImShoppingCartSerializer,
    CreateNewImportCartObjectSerializer
)
from products.models import (
    StoreProduct
)


######################################################################################
# --------------- IMPORT SHOPPING CART -------------------------------------------------------------
######################################################################################

# --------------- Get Current Import Shopping Cart ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_current_import_shopping_cart(request):
    user = request.user

    if request.method == "GET":
        im_shopping_cart_obj = ImShoppingCartObject.objects.get(account=user, status="current")
        import_products = ImportProduct.objects.filter(im_shopping_car_obj=im_shopping_cart_obj)
        shopping_cart_ser = ImShoppingCartObjSerializer(im_shopping_cart_obj)
        im_prods_ser = ImportProductsSerializer(import_products, many=True)
        data = {}
        data["shopping_cart_obj"] = shopping_cart_ser.data
        data["import_products"] = im_prods_ser.data

    return Response(data)


# --------------- Add Product To Import Cart ---------------
# @api_view(["POST"])
# @permission_classes((IsAuthenticated,))
# def addProductToImportCart(request, store_product_id):
#     user = request.user
#
#     if request.method == "POST":
#         current_cart_object = ImShoppingCartObject.objects.get(status="current")
#         if current_cart_object is None:
#             new_current_object = ImShoppingCartObject()
#             new_current_object.status = "current"
#             new_current_object.account = user
#
#             new_import_objc_ser = ImportShoppingCartEmptySerializer(new_current_object, data=request.data)
#
#             if new_import_objc_ser.is_valid():
#                 new_import_objc_ser.save()
#                 store_product = StoreProduct.objects.get(product_id=store_product_id)
#
#                 new_cart_product = ImportProduct()
#                 new_cart_product.im_shopping_car_obj = new_current_object
#                 new_cart_product.import_product = store_product


# --------------- Get Current Import Object ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_current_import_object(request):
    user = request.user

    if request.method == "GET":
        data = {}

        try:
            import_object = ImShoppingCartObject.objects.get(account=user, status="current")
            if import_object is not None:
                data["import_object"] = "exist"
        except ObjectDoesNotExist:
            data["import_object"] = "none"



        return Response(data=data)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_import_cart_object(request):
    user = request.user

    # if request.method == "POST":
    # ser = CreateNewImportCartObjectSerializer(data=request.data)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def add_product_to_import_cart(request):
    user = request.user

    if request.method == "POST":
        ser = AddProdToImShoppingCartSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
