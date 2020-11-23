from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import UpdateAPIView

from .models import (
    Account
)
from .serializers import (
    AccountSerializer,
    AccountPropertiesSerializer,
    ChangePasswordSerializer
)


# --------------- COMMON -------------------------------------------------------------

# --------------- Get All Accounts ---------------

@api_view(["GET"])
# @permission_classes((IsAuthenticated,))
def get_all_accounts(request):
    accounts = Account.objects.all()
    ser = AccountSerializer(accounts, many=True)
    return Response(ser.data)


# --------------- AUTH -------------------------------------------------------------

# --------------- Registration New User ---------------

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


# --------------- PROFILE -------------------------------------------------------------

# --------------- Get Profile Info ---------------

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_profile_info(request):
    user = request.user  # Gives me a user which made request
    account = Account.objects.get(account_id=user.account_id)
    ser = AccountPropertiesSerializer(account)
    return Response(ser.data)


# --------------- Edit Profile Data ---------------

@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def put_one_account(request):
    user = request.user
    try:
        account = Account.objects.get(account_id=user.account_id)
    except Account.DoesNotExixt:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        # print("--------account" + str(account))
        ser = AccountPropertiesSerializer(account, data=request.data, partial=True)
        data = {}
        if ser.is_valid():
            ser.save()
            data["status"] = "update success"
            return Response(data=data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------- Change Password ---------------

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




