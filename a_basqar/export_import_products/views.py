from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from export_import_products.models import (
    ImportProducts,
    ImShoppingCartObject
)
from rest_framework.response import Response

from export_import_products.serializer import (
    ImportProductsSerializer,
    ImShoppingCartObjSerializer
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
        import_products = ImportProducts.objects.filter(im_shopping_car_obj=im_shopping_cart_obj)
        shopping_cart_ser = ImShoppingCartObjSerializer(im_shopping_cart_obj)
        im_prods_ser = ImportProductsSerializer(import_products, many=True)
        data = {}
        data["shopping_cart_obj"] = shopping_cart_ser.data
        data["import_products"] = im_prods_ser.data

    return Response(data)