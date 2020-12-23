from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from .models import (
    IncomeKassaObject
)
from .serializer import (
    IncomeKassaObjectSerializer,
    GetIncomeKassaHistoryObjectsSerializer,
    # CreateNewIncomeKassaObjectSerializer,
    CreateNewIncomeKassaWithContragent,
    CreateNewIncomeKassaWithExport
)
from company_management.models import (
    Contragent
)
from export_import_products.models import (
    ExShoppingCartObject
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


# --------------- Create New Income Kassa History Objects ---------------
# @api_view(["POST"])
# @permission_classes((IsAuthenticated,))
# def create_new_income_kassa(request):
    # global cash_sum, contragent, export_object, comment
    # user = request.user
    #
    # if request.data["contragent"] is not None:
    #     try:
    #         contragent = Contragent.objects.get(contragent_id=request.data["contragent"])
    #     except ObjectDoesNotExist:
    #         contragent = None
    #
    # if request.data["export_object"] is not None:
    #     try:
    #         export_object = ExShoppingCartObject.objects.get(ex_shopping_cart_id=request.data["export_object"])
    #         contragent = export_object.export_contragent
    #         cash_sum = export_object.cash_sum
    #     except ObjectDoesNotExist:
    #         export_object = None
    #
    # if request.data["comment"] is not None:
    #     comment = request.data["comment"]
    # else:
    #     comment = None
    #
    # income_kassa = IncomeKassaObject()
    # income_kassa.income_name = ""
    # income_kassa.income_status = "history"
    # income_kassa.fact_cash = request.data["fact_cash"]
    # income_kassa.cash_sum = request.data["fact_cash"]
    # income_kassa.comment = request.data["comment"]
    # income_kassa.contragent = contragent
    # income_kassa.export_object = export_object
    #
    # # ///////////////
    # if cash_sum is not None:
    #     income_kassa.cash_sum = cash_sum
    # else:
    #     income_kassa.cash_sum = request.data["fact_cash"]
    # if comment is not None:
    #     income_kassa.comment = comment
    # if contragent is not None:
    #     income_kassa.contragent = contragent
    # if export_object is not None:
    #     income_kassa.export_object = export_object
    # # //////////////
    # income_kassa.date = datetime.date(datetime.now())
    # income_kassa.account = user
    #
    # if request.method == "POST":
    #     data = {}
    #
    #     ser = CreateNewIncomeKassaObjectSerializer(income_kassa, data=request.data)
    #     test_ser = IncomeKassaObjectSerializer(income_kassa)
    #     if ser.is_valid():
    #         # ser.save()
    #         data["message"] = "success"
    #         data["desc"] = "successfully created new kassa object to history"
    #         data["data"] = ser.data
    #         data["test_data"] = test_ser.data
    #     else:
    #         data["message"] = "not valid ser"
    #         data["desc"] = ser.data
    #     # print("///"+str(ser.errors))
    #     return Response(data=data)

# --------------- Create New Income Kassa History Objects Wit Export Object ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_income_kassa_contr(request):
    user = request.user

    if request.method == "POST":
        data = {}
        if request.data["contragent"] is not None:
            contragent = Contragent.objects.get(contragent_id=request.data["contragent"])
            income_kassa_obj = create_new_income_kassa_object(fact_cash=request.data["fact_cash"],
                                                              cash_sum=request.data["fact_cash"],
                                                              contragent=contragent,
                                                              export_object=None,
                                                              comment=request.data["comment"],
                                                              account=user
                                                              )
            cont_ser = CreateNewIncomeKassaWithContragent(income_kassa_obj, data=request.data)
            test_ser = IncomeKassaObjectSerializer(income_kassa_obj)
            if cont_ser.is_valid():
                cont_ser.save()
                data["message"] = "success"
                data["desc"] = "successfully created new kassa object to history"
                data["data"] = cont_ser.data
                data["test_data"] = test_ser.data
            else:
                data["message"] = "not valid ser"
                data["desc"] = cont_ser.data
            print("///"+str(cont_ser.errors))
            return Response(data=data)







def create_new_income_kassa_object(fact_cash, cash_sum, contragent, export_object, comment, account):
    income_kassa_object = IncomeKassaObject()
    income_kassa_object.income_name = ""
    income_kassa_object.income_status = "history"
    income_kassa_object.fact_cash = fact_cash
    if cash_sum == "":
        income_kassa_object.cash_sum = fact_cash
    else:
        income_kassa_object.cash_sum = cash_sum
    income_kassa_object.contragent = contragent
    income_kassa_object.export_object = export_object
    income_kassa_object.comment = comment
    income_kassa_object.account = account
    income_kassa_object.date = datetime.date(datetime.now())

    return income_kassa_object