from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import (
    Company,
    Store
)
from .serializers import (
    CompanySerializer,
    StoreSerializer
)

# Create your views here.

# --------------- STORES -------------------------------------------------------------

# --------------- Get All User's Company Stores ---------------

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_all_users_company_stores(request):
    user = request.user
    stores = Store.objects.filter(store_id=user.store_id)
    ser = StoreSerializer(stores, many=True)
    return Response(ser.data)


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