from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import (
    CommonCategory,
    CompanyCategory,
    CommonProduct,
    CompanyProduct,
    StoreProduct
)

from .serializer import (
    CommonCategorySerializer,
    EachCompanyCategorySerializer,
    CommonProductSerializer,
    EachCompanyProductSerializer,
    EachStoreProductProductSerializer,
)

from account.models import Account
from account.serializers import AccountPropertiesSerializer
from company_management.models import Company, Store
from company_management.serializers import CompanySerializer, StoreSerializer

######################################################################################
# --------------- COMMON -------------------------------------------------------------
######################################################################################

# --------------- Get All Common Categories ---------------
@api_view(["GET"])
def get_all_common_categories(request):
    common_categories = CommonCategory.objects

    if request.method == "GET":
        ser = CommonCategorySerializer(common_categories, many=True)

    return Response(ser.data)

# --------------- Get Each Company Categories ---------------
# --------------- Get All Common Products ---------------
# --------------- Get Each Company Products ---------------
# --------------- Get Each Store Products ---------------


######################################################################################
# --------------- EACH COMPANY PRODUCT MANAGEMENT -------------------------------------------------------------
######################################################################################

# --------------- Get Each Company Categories ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_each_company_categories(request):
    user = request.user

    if request.method == "GET":
        account = Account.objects.get(account_id=user.account_id)
        company = Company.objects.get(company_id=account.company.company_id)
        company_category = CompanyCategory.objects.filter(category_company=company)
        ser = EachCompanyCategorySerializer(company_category, many=True)

    return Response(ser.data)


# --------------- Get Each Company Products ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_each_company_products_in_selected_category(request, category_id):
    user = request.user

    if request.method == "GET":
        company_category = CompanyCategory.objects.get(category_id=category_id)
        products_in_selected_category = CompanyProduct.objects.filter(product_category=company_category)
        ser = EachCompanyProductSerializer(products_in_selected_category, many=True)
    return Response(ser.data)