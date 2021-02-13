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
    CreateCompanyProductSerializer,
    EditCompanyProductExportAndImportSerializer,
    CreateStoreProductsSerializer,
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


# --------------- Add Category From Common To Company ---------------
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
        new_company_category.category_index_id = common_category.category_index_id

        new_company_category.category_company = company

        ser = CreateCompanyCategorySerializer(new_company_category, data=request.data)
        if ser.is_valid():
            ser.save()
            data = {"status": "success"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------- Add Products From Common To Company ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def add_products_from_common_to_company(request, common_product_id):
    user = request.user

    if request.method == "POST":
        try:
            common_product = CommonProduct.objects.get(product_id=common_product_id)
        except CommonProduct.DoesNotExixt:
            return Response(status=status.HTTP_404_NOT_FOUND)

        company = Company.objects.get(company_id=user.company_id)
        common_category = CommonCategory.objects.get(
            category_index_id=common_product.product_category.category_index_id)

        try:
            company_category = CompanyCategory.objects.get(category_index_id=common_category.category_index_id)
        except CompanyCategory.DoesNotExixt:
            return Response(status=status.HTTP_404_NOT_FOUND)

        new_company_product = CompanyProduct()
        new_company_product.product_name = common_product.product_name
        common_product_category = company_category
        new_company_product.product_category = common_product_category

        new_company_product.product_barcode = ""
        new_company_product.product_export_price = 0
        new_company_product.product_import_price = 0
        new_company_product.product_company = company

        ser = CreateCompanyProductSerializer(new_company_product, data=request.data)
        if ser.is_valid():
            ser.save()
            data = {"status": "success"}
            return Response(data=data, status=status.HTTP_201_CREATED)


# --------------- Edit Products Import/Export Prices ---------------
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def edit_prods_import_export_prices(request, product_id):
    user = request.user

    try:
        company_product = CompanyProduct.objects.get(product_id=product_id)
    except CompanyProduct.DoesNotExixt:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        ser = EditCompanyProductExportAndImportSerializer(company_product, data=request.data, partial=True)
        data = {}
        if ser.is_valid():
            ser.save()
            data["status"] = "success"
            return Response(data=data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

