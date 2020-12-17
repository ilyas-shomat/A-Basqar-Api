from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    ImportProduct,
    ImShoppingCartObject,
    ExportProduct,
    ExShoppingCartObject
)
from .serializer import (
    ImportProductsSerializer,
    ImShoppingCartObjSerializer,
    AddProdToImShoppingCartSerializer,
    CreateNewImportCartObjectSerializer,
    EditProductCountInImportCartSerializer,
    ExportProductsSerializer,
    ExShoppingCartObjSerializer,
    AddProdToExShoppingCartSerializer,
    CreateNewExportCartObjectSerializer,
    EditProductCountInExportCartSerializer
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
        data = {"shopping_cart_obj": shopping_cart_ser.data, "import_products": im_prods_ser.data}

    return Response(data)


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


# --------------- Create New Import Cart Object ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_import_cart_object(request):
    user = request.user

    if request.method == "POST":
        data = {}
        ser = CreateNewImportCartObjectSerializer(data=request.data)
        if ser.is_valid():
            try:
                import_object = ImShoppingCartObject.objects.get(account=user, status="current")
                if import_object is not None:
                    data["import_object"] = "exist"
                    data["desc"] = "object already exist"
            except ObjectDoesNotExist:
                new_import_obj = ImShoppingCartObject()
                new_import_obj.account = user
                new_import_obj.status = "current"
                new_import_obj.save()

                data["import_object"] = "created"
                data["desc"] = "created new current import object"

        return Response(data=data)


# --------------- Add Product to Import Cart ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def add_product_to_import_cart(request):
    user = request.user
    product = StoreProduct.objects.get(product_id=request.data["import_product"])
    import_cart_object = ImShoppingCartObject(im_shopping_cart_id=request.data["im_shopping_car_obj"])
    if request.method == "POST":
        data = {}

        import_prods = ImportProduct.objects.filter(im_shopping_car_obj=import_cart_object)
        for prod in import_prods:
            if prod.import_product.product_id == request.data["import_product"]:
                #################### This code be useful in future
                # amount_in_cart = 2 * prod.prod_amount_in_cart
                # prod.prod_amount_in_cart = prod.prod_amount_in_cart + request.data["prod_amount_in_cart"]
                # prod_ser = AddProdToImShoppingCartSerializer(prod, data=request.data)
                #
                # if prod_ser.is_valid():
                #     prod_ser.save()

                data["message"] = "exist"
                data["desc"] = "this import_product is already exist in import cart"
                return Response(data=data)

        import_prod = ImportProduct()
        import_prod.import_product = product
        import_prod.im_shopping_car_obj = import_cart_object

        ser = AddProdToImShoppingCartSerializer(import_prod, data=request.data)

        if ser.is_valid():
            ser.save()
            data["message"] = "added"
            data["desc"] = "import_product added to the cart"

        return Response(data=data)


# --------------- Edit Product Count in Import Cart ---------------
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def edit_product_count_in_import_cart(request):
    import_product = ImportProduct.objects.get(im_prod_id=request.data["im_prod_id"])

    if request.method == "PUT":
        data = {}
        import_product.prod_amount_in_cart = request.data["prod_amount_in_cart"]
        ser = EditProductCountInImportCartSerializer(import_product, data=request.data)

        if ser.is_valid():
            print("/// entire the ser")

            ser.save()
            data["message"] = "edited"
            data["desc"] = "import_product's amount count edited"

        return Response(data=data)


# --------------- Delete Product Count in Import Cart ---------------
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_product_count_in_import_cart(request):
    import_product = ImportProduct.objects.get(im_prod_id=request.data["im_prod_id"])

    if request.method == "DELETE":
        data = {}
        operation = import_product.delete()

        if operation:
            data["message"] = "deleted"
            data["desc"] = "selected import_product deleted"
        else:
            data["message"] = "failed"
            data["desc"] = "failed deleting selected import_product"
        return Response(data=data)


######################################################################################
# --------------- EXPORT SHOPPING CART -------------------------------------------------------------
######################################################################################

# --------------- Get Current Export Shopping Cart ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_current_export_shopping_cart(request):
    user = request.user

    if request.method == "GET":
        ex_shopping_cart_obj = ExShoppingCartObject.objects.get(account=user, status="current")
        export_products = ExportProduct.objects.filter(ex_shopping_car_obj=ex_shopping_cart_obj)
        shopping_cart_ser = ExShoppingCartObjSerializer(ex_shopping_cart_obj)
        ex_prods_ser = ExportProductsSerializer(export_products, many=True)
        data = {"shopping_cart_obj": shopping_cart_ser.data, "export_products": ex_prods_ser.data}

    return Response(data)


# --------------- Get Current Export Object ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_current_export_object(request):
    user = request.user

    if request.method == "GET":
        data = {}
        try:
            export_object = ExShoppingCartObject.objects.get(account=user, status="current")
            if export_object is not None:
                data["export_object"] = "exist"
        except ObjectDoesNotExist:
            data["export_object"] = "none"

        return Response(data=data)


# --------------- Create New Export Cart Object ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_export_cart_object(request):
    user = request.user

    if request.method == "POST":
        data = {}
        ser = CreateNewExportCartObjectSerializer(data=request.data)
        if ser.is_valid():
            try:
                export_object = ExShoppingCartObject.objects.get(account=user, status="current")
                if export_object is not None:
                    data["export_object"] = "exist"
                    data["desc"] = "object already exist"
            except ObjectDoesNotExist:
                new_export_obj = ExShoppingCartObject()
                new_export_obj.account = user
                new_export_obj.status = "current"
                new_export_obj.save()

                data["import_object"] = "created"
                data["desc"] = "created new current import object"

        return Response(data=data)

# --------------- Add Product to Export Cart ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def add_product_to_export_cart(request):
    user = request.user
    product = StoreProduct.objects.get(product_id=request.data["export_product"])
    export_cart_object = ExShoppingCartObject(ex_shopping_cart_id=request.data["ex_shopping_car_obj"])
    if request.method == "POST":
        data = {}

        export_prods = ExportProduct.objects.filter(ex_shopping_car_obj=export_cart_object)
        for prod in export_prods:
            if prod.export_product.product_id == request.data["export_product"]:
                data["message"] = "exist"
                data["desc"] = "this export_product is already exist in import cart"
                return Response(data=data)

        export_prod = ExportProduct()
        export_prod.export_product = product
        export_prod.im_shopping_car_obj = export_cart_object

        ser = AddProdToExShoppingCartSerializer(export_prod, data=request.data)

        if ser.is_valid():
            ser.save()
            data["message"] = "added"
            data["desc"] = "import_product added to the cart"

        return Response(data=data)


# --------------- Edit Product Count in Export Cart ---------------
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def edit_product_count_in_export_cart(request):
    export_product = ExportProduct.objects.get(ex_prod_id=request.data["ex_prod_id"])

    if request.method == "PUT":
        data = {}
        export_product.prod_amount_in_cart = request.data["prod_amount_in_cart"]
        ser = EditProductCountInExportCartSerializer(export_product, data=request.data)

        if ser.is_valid():
            ser.save()
            data["message"] = "edited"
            data["desc"] = "export_product's amount count edited"

        return Response(data=data)


# --------------- Delete Product Count in Import Cart ---------------
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_product_count_in_export_cart(request):
    export_product = ExportProduct.objects.get(ex_prod_id=request.data["ex_prod_id"])

    if request.method == "DELETE":
        data = {}
        operation = export_product.delete()

        if operation:
            data["message"] = "deleted"
            data["desc"] = "selected import_product deleted"
        else:
            data["message"] = "failed"
            data["desc"] = "failed deleting selected export_product"
        return Response(data=data)