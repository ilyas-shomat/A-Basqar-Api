from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company, Store, Account
from .serializers import StoreSerializer, CompanySerializer, AccountSerializer
from rest_framework.authtoken.models import Token


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

# @api_view(["POST"])
# def login(request):

# ----------------COMMON-----------------------
@api_view(["GET"])
def get_all_accounts(request):
    accounts = Account.objects.all()
    ser = AccountSerializer(accounts, many=True)
    return Response(ser.data)



# ----------------LOGIN-----------------------


# ----------------PROFILE-----------------------

@api_view(["GET"])
def get_one_account(request, account_id):
    account = Account.objects.get(account_id=account_id)
    ser = AccountSerializer(account)
    return Response(ser.data)

@api_view(["PUT"])
def put_one_account(request, account_id):

    try:
        account = Account.objects.get(account_id=account_id)
    except Account.DoesNotExixt:
        return  Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        ser = AccountSerializer(account, data=request.data)
        data = {}
        if ser.is_valid():
            ser.save()
            data["status"] = "update success"
            return Response(data=data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_one_account(request, account_id):

    try:
        account = Account.objects.get(account_id=account_id)
    except Account.DoesNotExixt:
        return  Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation  = account.delete()
        data = {}
        if operation:
            data["status"] = "delete success"
        else:
            data["status"] = "delete failed"
        return Response(data=data)

# Working code
# @api_view(["POST"])
# def post_one_account(request):
#
#     account  = Account.objects.get(account_id=1)
#
#     new_account = Account()
#
#     if request.method == "POST":
#         ser = AccountSerializer(new_account, data=request.data)
#
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def post_one_account(request):

    if request.method == 'POST':
        ser = AccountSerializer(data=request.data)
        data = {}
        if ser.is_valid():
            account = ser.save()
            data['reponse'] = 'success'
            data['full_name'] = account.full_name
            data['token'] = Token.objects.get(user=account).key
        else:
            data = ser.errors
        return Response(data)

# ---------------- EXPORT PRODUCTS --------------


@api_view(["GET"])
def get_post_companies(request):
    companies = Company.objects.all()
    ser = CompanySerializer(companies, many=True)
    return Response(ser.data)





@api_view(["GET"])
def get_stores(request, company_id):
    # cid = request.GET.get("pk")
    company = Company.objects.get(company_id=company_id)
    stores = Store.objects.filter(company=company)
    ser = StoreSerializer(stores, many=True)
    str = request.data.get("store")
    return Response(ser.data)
