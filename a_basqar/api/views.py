from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Company, Store, Account
from .serializers import (StoreSerializer,
                          CompanySerializer,
                          AccountSerializer,
                          AccountPropertiesSerializer,
                          ChangePasswordSerializer)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import UpdateAPIView


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
@permission_classes((IsAuthenticated,))
def get_all_accounts(request):
    accounts = Account.objects.all()
    ser = AccountSerializer(accounts, many=True)
    return Response(ser.data)


# ---------------- AUTH -----------------------

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


# ----------------PROFILE-----------------------

# ----------------Get Profile Info-----------------------

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_profile_info(request):
    user = request.user  # Gives me a user which made request
    # print("------------"+str(user.password))
    account = Account.objects.get(account_id=user.account_id)
    ser = AccountPropertiesSerializer(account)
    return Response(ser.data)


# @api_view(["GET"])
# def get_one_account(request, account_id):
#     account = Account.objects.get(account_id=account_id)
#     ser = AccountSerializer(account)
#     return Response(ser.data)


# ----------------Edit Profile Data-----------------------

@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def put_one_account(request):
    user = request.user
    try:
        account = Account.objects.get(account_id=user.account_id)
    except Account.DoesNotExixt:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        print("--------account" + str(account))
        ser = AccountPropertiesSerializer(account, data=request.data, partial=True)
        data = {}
        if ser.is_valid():
            ser.save()
            data["status"] = "update success"
            return Response(data=data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------Change Password-----------------------

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"response": "successfully changed password"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["DELETE"])
# def delete_one_account(request, account_id):
#     try:
#         account = Account.objects.get(account_id=account_id)
#     except Account.DoesNotExixt:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "DELETE":
#         operation = account.delete()
#         data = {}
#         if operation:
#             data["status"] = "delete success"
#         else:
#             data["status"] = "delete failed"
#         return Response(data=data)


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
