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
    CreateCompanyCategorySerializer,
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


# --------------- Get Each Company Categories ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def add_company_category_from_common_category(request, common_category_id):
    user = request.user

    if request.method == "POST":
        try:
            common_category = CommonCategory.objects.get(category_id=common_category_id)
        except CommonCategory.DoesNotExixt:
            return Response(status=status.HTTP_404_NOT_FOUND)

        company = Company.objects.get(company_id=user.company_id)
        new_company_category = CompanyCategory()
        new_company_category.category_name = common_category.category_name
        new_company_category.category_level = common_category.category_level

        new_company_category.category_company = company

        ser = CreateCompanyCategorySerializer(new_company_category, data=request.data)
        if ser.is_valid():
            ser.save()
            data = {}
            data["status"] = "success"
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)






