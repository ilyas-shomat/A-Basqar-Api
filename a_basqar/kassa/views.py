from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    IncomeKassaObject
)
from .serializer import (
    IncomeKassaObjectSerializer,
    GetIncomeKassaHistoryObjectsSerializer,
)

######################################################################################
# --------------- INCOME KASSA -------------------------------------------------------------
######################################################################################

# --------------- Get Income Kassa Objects List ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_income_kassa_objects(request):
    user = request.user

    if request.method == "GET":
        income_objects = IncomeKassaObject.objects.filter(account=user)
        ser = IncomeKassaObjectSerializer(income_objects, many=True)
        return Response(ser.data)

# --------------- Get Income Kassa History Objects ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_income_kassa_history_objects(request):
    user = request.user

    if request.method == "GET":
        income_objects = IncomeKassaObject.objects.filter(account=user, income_status="history")
        ser = GetIncomeKassaHistoryObjectsSerializer(income_objects, many=True)
        return Response(ser.data)