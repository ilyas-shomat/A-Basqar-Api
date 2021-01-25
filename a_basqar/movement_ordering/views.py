from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime

from .models import (
    MovementObject,
    MovementProduct,
    OrderingObject, 
    OrderingProduct
)

from .serializer import (
    MovementObjectSerializer,
    MovementProductsSerializer,
    CreateNewMovementObjectSerializer,
    AddProdToMovementCartSerializer,
    EditProductCountInMovementCartSerializer,
    MakeMovementHistorySerializer,
    OrderingObjectSerialzer,
    OrderingProductsSerializer,
    CreateNewOrderingSerializer,
    AddProdToOrderingCartSerializer,
    EditProductCountInOrderingCartSerializer,
    MakeOrderingOpenSerializer,
    MakeOrderingHistorySerilizer
)

from products.models import (
    StoreProduct
)

from account.models import (
    Store
)

######################################################################################
# --------------- MOVEMENT -------------------------------------------------------------
######################################################################################

# --------------- Get Current Movement Object ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_current_movement_object(request):
    account = request.user

    if request.method == "GET":
        data = {}

        try:
            movement_object = MovementObject.objects.get(account=account, status="current")
            data["import_object"] = "exist"

        except ObjectDoesNotExist:
            data["import_object"] = "none"

        return Response(data=data)


# --------------- Get Movement Cart ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_movement_cart(request):
    account = request.user

    if request.method == "GET":
        data = {}
        try:
            movement_object = MovementObject.objects.get(account=account, status="current")
            movement_ser = MovementObjectSerializer(movement_object)
            movement_products = MovementProduct.objects.filter(movement_object=movement_object)
            movement_product_ser = MovementProductsSerializer(movement_products, many=True)
            data = {"movement_object": movement_ser.data, "movement_products": movement_product_ser.data}
        except ObjectDoesNotExist:
            data["message"] = "empty"
            data["desc"] = "movement cart is empty"
    
    return Response(data)

# --------------- Create New Movement Cart ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_movement_cart(request):
    account = request.user

    if request.method == "POST":
        data = {}
        ser = CreateNewMovementObjectSerializer(data=request.data)
        if ser.is_valid():
            try:
                movement_object = MovementObject.objects.get(account=account, status="current")
                if movement_object is not None:
                    data["movement_object"] = "exist"
                    data["desc"] = "object already exist"
            except ObjectDoesNotExist:
                new_movement_object = MovementObject()
                new_movement_object.account = account
                new_movement_object.status = "current"
                new_movement_object.save()          

                data["movement_object"] = "created"
                data["desc"] = "created new current movement object"
        
        return Response(data=data)


# --------------- Add Product to Movement Cart ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def add_product_to_movement_cart(request):
    account = request.user
    product = StoreProduct.objects.get(product_id=request.data["movement_product"])
    movement_object = MovementObject.objects.get(account=account, status="current")

    if request.method == "POST":
        data = {}

        movement_prods = MovementProduct.objects.filter(movement_object=movement_object)
        for prod in movement_prods:
            if prod.movement_product.product_id == request.data["movement_product"]:
                data["message"] = "exist"
                data["desc"] = "this import_product is already exist in movement cart"
                return Response(data=data)
        
        movement_prod = MovementProduct()
        movement_prod.movement_product = product
        movement_prod.movement_object = movement_object
        movement_prod.account = account
        movement_prod.date = datetime.date(datetime.now())

        ser = AddProdToMovementCartSerializer(movement_prod, data=request.data)

        if ser.is_valid():
            ser.save()
            data["message"] = "added"
            data["desc"] = "import_product added to the cart"

        return Response(data=data)


# --------------- Edit Product Count in Movement Cart ---------------
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def edit_product_count_in_movement_cart(request):
    movement_product = MovementProduct.objects.get(movement_prod_id=request.data["movement_prod_id"])

    if request.method == "PUT":
        data = {}
        movement_product.product_amount = request.data["product_amount"]
        ser = EditProductCountInMovementCartSerializer(movement_product, data=request.data)
        
        print("/// entire the func")

        if ser.is_valid():
            ser.save()
            data["message"] = "edited"
            data["desc"] = "import_product's amount count edited"

        return Response(data=data)


# --------------- Delete Product Count in Movement Cart ---------------
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_product_count_in_movement_cart(request):
    movement_product = MovementProduct.objects.get(movement_prod_id=request.data["movement_prod_id"])

    if request.method == "DELETE":
        data = {}

        operation = movement_product.delete()

        if operation:
            data["message"] = "deleted"
            data["desc"] = "selected movement product deleted"
        else:
            data["message"] = "failed"
            data["desc"] = "failed deleting selected movement product"
        return Response(data=data)


# --------------- Make Movement History (Send Prods from one to other Store) ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def make_movement_history(request):
    account = request.user
    store = Store.objects.get(store_id=request.data["store_id"])
    if request.method == "POST":
        data = {}
        try:
            current_movement = MovementObject.objects.get(account=account, status="current")
            current_movement.store = store
            current_movement.status = "history"
            current_movement.date = datetime.date(datetime.now())

            ser = MakeMovementHistorySerializer(current_movement, data=request.data)

            if ser.is_valid():
                ser.save()
                data["message"] = "success"
                data["desc"] = "successfully changed movement object from current to history"

        except ObjectDoesNotExist:
            data["message"] = "failure"
            data["desc"] = "movement object with status=current not found"

        return Response(data=data)


# --------------- Get Movement History ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_movement_history(request):
    account = request.user

    if request.method == "GET":
        movement_object = MovementObject.objects.filter(account=account, status="history")
        ser = MovementObjectSerializer(movement_object, many = True)
        return Response(ser.data)


# --------------- Get Movement History Item ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_movement_history_item(request, movement_id):
    account = request.user

    if request.method == "GET":
        movement_object = MovementObject.objects.get(movement_id=movement_id)
        ser = MovementObjectSerializer(movement_object)
        return Response(ser.data)



######################################################################################
# --------------- ORDERING -------------------------------------------------------------
######################################################################################

# --------------- Get Current Ordering Object ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_current_ordering_object(request):
    account = request.user

    if request.method == "GET":
        data = {}

        try:
            ordering_object = OrderingObject.objects.get(account=account, status="current")
            data["import_object"] = "exist"

        except ObjectDoesNotExist:
            data["import_object"] = "none"

        return Response(data=data)


# --------------- Get Ordering Cart ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_ordering_cart(request):
    account = request.user

    if request.method == "GET":
        data = {}
        try:
            ordering_object = OrderingObject.objects.get(account=account, status="current")
            ordering_ser = OrderingObjectSerialzer(ordering_object)
            ordering_products = OrderingProduct.objects.filter(ordering_object=ordering_object)
            ordering_product_ser = OrderingProductsSerializer(ordering_products, many=True)
            data = {"ordering_object": ordering_ser.data,  "ordering_products": ordering_product_ser.data}
        except ObjectDoesNotExist:
            data["message"] = "empty"
            data["desc"] = "movement cart is empty"

    return Response(data)


# --------------- Create New Ordering Cart ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_ordering_cart(request):
    account = request.user

    if request.method == "POST":
        data = {}
        ser = CreateNewOrderingSerializer(data=request.data)
        if ser.is_valid():
            try: 
                ordering_object = OrderingObject.objects.get(account=account, status="current")
                if ordering_object is not None:
                    data["ordering_object"] = "exist"
                    data["desc"] = "object already exist"
            except ObjectDoesNotExist:
                new_ordering_object = OrderingObject()
                new_ordering_object.account = account
                new_ordering_object.status = "current"
                new_ordering_object.save()

                data["movement_object"] = "created"
                data["desc"] = "created new current movement object"
        
        return Response(data=data)


# --------------- Add Product to Ordering Cart ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def add_product_to_ordering_cart(request):
    account = request.user
    product = StoreProduct.objects.get(product_id=request.data["ordering_product"])
    ordering_object = OrderingObject.objects.get(account=account, status="current")

    if request.method == "POST":
        data = {}

        ordering_prods = OrderingProduct.objects.filter(ordering_object=ordering_object)
        for prod in ordering_prods:
            if prod.ordering_product.product_id == request.data["ordering_product"]:
                data["message"] = "exist"
                data["desc"] = "this ordering product is already exist in ordering cart"
                return Response(data=data)

        ordering_prod = OrderingProduct()
        ordering_prod.ordering_product = product
        ordering_prod.ordering_object = ordering_object
        ordering_prod.account = account
        ordering_prod.date = datetime.date(datetime.now())

        ser = AddProdToOrderingCartSerializer(ordering_prod, data=request.data)

        if ser.is_valid():
            ser.save()
            data["message"] = "added"
            data["desc"] = "ordering product added to the cart"

        return Response(data=data)

# --------------- Edit Product Count in Ordering Cart ---------------
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def edit_product_count_in_ordering_cart(request):
    ordering_product = OrderingProduct.objects.get(ordering_prod_id=request.data["ordering_prod_id"])

    if request.method == "PUT":
        data = {}
        ordering_product.product_amount = request.data["product_amount"]
        ser = EditProductCountInOrderingCartSerializer(ordering_product, data=request.data)
        
        if ser.is_valid():
            ser.save()
            data["message"] = "edited"
            data["desc"] = "ordering_product's amount count edited"

        return Response(data=data)


# --------------- Delete Product Count in Ordering Cart ---------------
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_product_count_in_ordering_cart(request):
    ordering_product = OrderingProduct.objects.get(ordering_prod_id=request.data["ordering_prod_id"])

    if request.method == "DELETE":
        data = {}

        operation = ordering_product.delete()

        if operation:
            data["message"] = "deleted"
            data["desc"] = "selected ordering product deleted"
        else:
            data["message"] = "failed"
            data["desc"] = "failed deleting selected ordering product"
        return Response(data=data)


# --------------- Make Ordering Object Open (Send Order to Orders List) ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def make_ordering_object_open(request):
    account = request.user

    if request.method == "POST":
        data = {}

        try:
            current_ordering = OrderingObject.objects.get(account=account, status="current")
            current_ordering.status = "open"
            current_ordering.date = datetime.date(datetime.now())

            ser = MakeOrderingOpenSerializer(current_ordering, data=request.data)

            if ser.is_valid():
                ser.save()
                data["message"] = "success"
                data["desc"] = "successfully changed ordering object from current to open"
        
        except ObjectDoesNotExist:
            data["message"] = "failure"
            data["desc"] = "ordering object with status=current not found"

        return Response(data=data)


# --------------- Make Ordering History (Send Order to Get New Movement) ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def make_ordering_history(request):
    account = request.user

    if request.method == "POST":
        data = {}

        try:
            current_ordering = OrderingObject.objects.get(account=account, ordering_id = request.data["ordering_id"])
            current_ordering.status = "history"
            current_ordering.date = datetime.date(datetime.now())

            ser = MakeOrderingOpenSerializer(current_ordering, data=request.data)

            if ser.is_valid():
                ser.save()
                data["message"] = "success"
                data["desc"] = "successfully changed ordering object from open to history"
        
        except ObjectDoesNotExist:
            data["message"] = "failure"
            data["desc"] = "ordering object with status=current not found"

        return Response(data=data)