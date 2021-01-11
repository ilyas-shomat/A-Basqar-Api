from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime

from .models import (
    MovementObject,
    MovementProduct
)

from .serializer import (
    MovementObjectSerializer,
    CreateNewMovementObjectSerializer,
    AddProdToMovementCartSerializer
)

from products.models import (
    StoreProduct
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
            data = {"movement_object": movement_ser.data}
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
                data["desc"] = "this import_product is already exist in import cart"
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