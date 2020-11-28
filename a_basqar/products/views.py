from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import (
    Common_Category,
    Each_Company_Category,
    Common_Product,
    Each_Company_Product,
    Each_Store_Product
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
    common_categories = Common_Category.objects

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
        each_company_category = Each_Company_Category.objects.filter(each_company_category_company=company)
        ser = EachCompanyCategorySerializer(each_company_category, many=True)

    return Response(ser.data)


# --------------- Get Each Company Products ---------------
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_each_company_products_in_selected_category(request, category_id):
    user = request.user

    if request.method == "GET":
        company_category = Each_Company_Category.objects.get(each_company_category_id=category_id)
        products_in_selected_category = Each_Company_Product.objects.filter(each_company_product_category=company_category)
        ser = EachCompanyProductSerializer(products_in_selected_category, many=True)
    return Response(ser.data)