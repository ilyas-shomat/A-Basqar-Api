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
    MovementObjectSerializer
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

