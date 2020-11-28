from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from account.serializers import AccountPropertiesSerializer

from .models import (
    Company,
    Store,
    AccessFunc
)
from .serializers import (
    CompanySerializer,
    StoreSerializer,
    AccessFuncsSerializer
)

######################################################################################
# --------------- COMPANIES -------------------------------------------------------------
######################################################################################

# --------------- Create New Company ---------------
@api_view(["POST"])
def registration_new_company(request):
    new_company = Company()

    if request.method == "POST":
        ser = CompanySerializer(new_company, data=request.data)

        if ser.is_valid():
            data = {}
            if ser.is_valid():
                ser.save()
                store = Store.objects.get(company=new_company)
                data["status"] = "success"
                data["company_id"] = new_company.company_id
                data["default_store_id"] = store.store_id
                return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------- Get Companies All Users ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_companies_all_user(request):
    user = request.user

    if request.method == "GET":
        company_id = user.company_id
        accounts = Account.objects.filter(company=company_id)
        ser = AccountPropertiesSerializer(accounts, many=True)

    return Response(ser.data)

# --------------- Get User From Companies Users List ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_user_from_companies_users_list(request, account_id):

    if request.method == "GET":
        accounts = Account.objects.get(account_id=account_id)
        ser = AccountPropertiesSerializer(accounts)

    return Response(ser.data)

# --------------- Get User's Access Funcs ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_users_access_funcs(request, account_id):

    if request.method == "GET":
        accounts = Account.objects.get(account_id=account_id)
        access_funcs = AccessFunc.objects.get(user=accounts)
        ser = AccessFuncsSerializer(access_funcs)

    return Response(ser.data)

# --------------- Edit User's Access Funcs ---------------
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def edit_users_access_funcs(request, account_id):
    try:
        account = Account.objects.get(account_id=account_id)
    except Account.DoesNotExixt:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        accesses = AccessFunc.objects.get(user=account)
        ser = AccessFuncsSerializer(accesses, data=request.data)
        data = {}
        if ser.is_valid():
            ser.save()
            data["status"] = "update success"
            return Response(data=data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


######################################################################################
# --------------- STORES -------------------------------------------------------------
######################################################################################


# --------------- Get All User's Company Stores ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_all_users_company_stores(request):
    user = request.user
    company = Company.objects.get(company_id=user.company_id)

    stores = Store.objects.filter(company=company.company_id)
    ser = StoreSerializer(stores, many=True)
    return Response(ser.data)


# --------------- Get Users List Of One Store ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_user_of_one_store(request, store_id):
    # print("///"+str(store_id))
    try:
        account = Account.objects.filter(store=store_id)
    except Account.DoesNotExixt:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ser = AccountPropertiesSerializer(account, many=True)

    return Response(ser.data)


# --------------- Create New Store  ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_new_store(request):
    user = request.user
    company = Company.objects.get(company_id=user.company_id)

    new_store = Store()
    new_store.company = company

    if request.method == "POST":
        ser = StoreSerializer(new_store, data=request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------- Update Store Info  ---------------
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def update_store_info(request, store_id):
    user = request.user
    try:
        store = Store.objects.get(store_id=store_id)
    except Store.DoesNotExixt:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        ser = StoreSerializer(store, data=request.data, partial=True)
        data = {}
        if ser.is_valid():
            ser.save()
            data["status"] = "update success"
            return Response(data=data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------- Delete Store  ---------------
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_one_account(request, store_id):
    try:
        store = Store.objects.get(store_id=store_id)
    except Store.DoesNotExixt:
        return  Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation  = store.delete()
        data = {}
        if operation:
            data["status"] = "delete success"
        else:
            data["status"] = "delete failed"
        return Response(data=data)

# @api_view(["GET"])
# @permission_classes((IsAuthenticated,))
# def get_post_companies(request):
#     companies = Company.objects.all()
#     ser = CompanySerializer(companies, many=True)
#     return Response(ser.data)
#
#
# @api_view(["GET"])
# @permission_classes((IsAuthenticated,))
# def get_stores(request, company_id):
#     # cid = request.GET.get("pk")
#     company = Company.objects.get(company_id=company_id)
#     stores = Store.objects.filter(company=company)
#     ser = StoreSerializer(stores, many=True)
#     str = request.data.get("store")
#     return Response(ser.data)
