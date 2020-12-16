from rest_framework import serializers

from .models import (
    CommonCategory,
    CompanyCategory,
    CommonProduct,
    CompanyProduct,
    StoreProduct
)


class CommonCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonCategory
        fields = "__all__"


class EachCompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = "__all__"


class CreateCompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = ()


class CommonProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonProduct
        fields = "__all__"


class EachCompanyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProduct
        fields = "__all__"


class CreateCompanyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProduct
        fields = ()


class CreateStoreProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProduct
        fields = "__all__"


class EditCompanyProductExportAndImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProduct
        fields = ('product_import_price', 'product_export_price')


class EachStoreProductProductSerializer(serializers.ModelSerializer):
    company_product = EachCompanyProductSerializer(read_only=True)

    class Meta:
        model = StoreProduct
        fields = "__all__"
