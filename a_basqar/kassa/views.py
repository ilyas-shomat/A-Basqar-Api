from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from .models import (
    IncomeKassaObject,
    ExpenseKassaObject
)
from .serializer import (
    IncomeKassaObjectSerializer,
    GetIncomeKassaHistoryObjectsSerializer,
    CreateNewIncomeKassaWithContragentSerializer,
    CreateNewIncomeKassaWithExportSerializer,
    ExpenseKassaObjectSerializer,
    GetExpenseKassaHistoryObjectsSerializer,
    CreateNewExpenseKassaWithContragentSerializer,
    CreateNewExpenseKassaWithImportSerializer
)
from company_management.models import (
    Contragent
)
from export_import_products.models import (
    ExShoppingCartObject,
    ImShoppingCartObject
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


# --------------- Create New Income Kassa History Objects Wit Contragent ---------------
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
            cont_ser = CreateNewIncomeKassaWithContragentSerializer(income_kassa_obj, data=request.data)
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
            print("///" + str(cont_ser.errors))
            return Response(data=data)


# --------------- Create New Income Kassa History Objects Wit Export Object ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_income_kassa_export(request):
    global cash_sum, contragent
    user = request.user

    if request.method == "POST":
        data = {}
        if request.data["export_object"] is not None:
            try:
                export_object = ExShoppingCartObject.objects.get(ex_shopping_cart_id=request.data["export_object"])
                contragent = export_object.export_contragent
                cash_sum = export_object.cash_sum
            except ObjectDoesNotExist:
                data["message"] = "failure"
                data["desc"] = "this export object doesn't exist"

            income_kassa_obj = create_new_income_kassa_object(fact_cash=request.data["fact_cash"],
                                                              cash_sum=cash_sum,
                                                              contragent=None,
                                                              export_object=export_object,
                                                              comment=request.data["comment"],
                                                              account=user
                                                              )
            export_ser = CreateNewIncomeKassaWithExportSerializer(income_kassa_obj, data=request.data)
            test_ser = IncomeKassaObjectSerializer(income_kassa_obj)
            if export_ser.is_valid():
                export_ser.save()
                data["message"] = "success"
                data["desc"] = "successfully created new kassa object to history"
                data["data"] = export_ser.data
                data["test_data"] = test_ser.data
            else:
                data["message"] = "not valid ser"
                data["desc"] = export_ser.data
            print("///" + str(export_ser.errors))
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


######################################################################################
# --------------- EXPENSE KASSA -------------------------------------------------------------
######################################################################################

# --------------- Get Expense Kassa History Objects ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_expense_kassa_history_objects(request):
    user = request.user

    if request.method == "GET":
        expense_objects = ExpenseKassaObject.objects.filter(account=user, expense_status="history")
        ser = GetExpenseKassaHistoryObjectsSerializer(expense_objects, many=True)
        return Response(ser.data)


# --------------- Create New Expense Kassa History Objects Wit Contragent ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_expense_kassa_contr(request):
    user = request.user

    if request.method == "POST":
        data = {}
        if request.data["contragent"] is not None:
            contragent = Contragent.objects.get(contragent_id=request.data["contragent"])
            expense_kassa_obj = create_new_expense_kassa_object(fact_cash=request.data["fact_cash"],
                                                                cash_sum=request.data["fact_cash"],
                                                                contragent=contragent,
                                                                import_object=None,
                                                                comment=request.data["comment"],
                                                                account=user
                                                                )
            cont_ser = CreateNewExpenseKassaWithContragentSerializer(expense_kassa_obj, data=request.data)
            test_ser = ExpenseKassaObjectSerializer(expense_kassa_obj)
            if cont_ser.is_valid():
                cont_ser.save()
                data["message"] = "success"
                data["desc"] = "successfully created new kassa object to history"
                data["data"] = cont_ser.data
                data["test_data"] = test_ser.data
            else:
                data["message"] = "not valid ser"
                data["desc"] = cont_ser.data
            print("///" + str(cont_ser.errors))
            return Response(data=data)


# --------------- Create New Expense Kassa History Objects Wit Export Object ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_expense_kassa_import(request):
    global cash_sum, contragent
    user = request.user

    if request.method == "POST":
        data = {}
        if request.data["import_object"] is not None:
            try:
                import_object = ImShoppingCartObject.objects.get(im_shopping_cart_id=request.data["import_object"])
                contragent = import_object.import_contragent
                cash_sum = import_object.cash_sum
            except ObjectDoesNotExist:
                data["message"] = "failure"
                data["desc"] = "this export object doesn't exist"

            import_kassa_obj = create_new_expense_kassa_object(fact_cash=request.data["fact_cash"],
                                                              cash_sum=cash_sum,
                                                              contragent=None,
                                                              import_object=import_object,
                                                              comment=request.data["comment"],
                                                              account=user
                                                              )
            export_ser = CreateNewExpenseKassaWithImportSerializer(import_kassa_obj, data=request.data)
            test_ser = ExpenseKassaObjectSerializer(import_kassa_obj)
            if export_ser.is_valid():
                export_ser.save()
                data["message"] = "success"
                data["desc"] = "successfully created new kassa object to history"
                data["data"] = export_ser.data
                data["test_data"] = test_ser.data
            else:
                data["message"] = "not valid ser"
                data["desc"] = export_ser.data
            print("///" + str(export_ser.errors))
            return Response(data=data)


def create_new_expense_kassa_object(fact_cash, cash_sum, contragent, import_object, comment, account):
    expense_kassa_object = ExpenseKassaObject()
    expense_kassa_object.expense_name = ""
    expense_kassa_object.expense_status = "history"
    expense_kassa_object.fact_cash = fact_cash
    if cash_sum == "":
        expense_kassa_object.cash_sum = fact_cash
    else:
        expense_kassa_object.cash_sum = cash_sum
    expense_kassa_object.contragent = contragent
    expense_kassa_object.export_object = import_object
    expense_kassa_object.comment = comment
    expense_kassa_object.account = account
    expense_kassa_object.date = datetime.date(datetime.now())

    return expense_kassa_object
